import os
import csv
import mimetypes
import numpy as np

from decimal import *

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from mltest.models import Input
from mltest.forms import InputForm, PredictForm
from mltest.LinearRegression import gradientDescent

# TODO: Bugs
# 1,2,3,4,5 vs 1,1,1,1,1

def indexView(request):
	context = RequestContext(request)

	if request.method == 'POST':	# Submit form
		form = InputForm(request.POST, request.FILES)

		if form.is_valid():
			userInput = form.save(commit=False)
			userInput.raw_file = request.FILES.get('raw_file')

			if (userInput.raw_file or 
				(userInput.raw_x and userInput.raw_y)):
				userInput.save()
				request.session['inputId'] = userInput.id;
				return HttpResponseRedirect('results/')
			else:
				error = "Need both X and Y data"
		else:		
			error = form.errors

		return render_to_response('mltest/error.html', 
			{'error': error}, context)

	else:  # Display form
		form = InputForm()
		return render_to_response('mltest/index.html', 
			{'inputForm': form}, context)

def resultsView(request):
	context = RequestContext(request)

	inputId = request.session.get('inputId')
	userInput = Input.objects.get(id=inputId)

	if userInput.raw_file:
		X, y, tblHeaders, error = cleanRawFile(userInput.raw_file, 
			userInput.filename())
	elif userInput.raw_x and userInput.raw_y:
		tblHeaders = ['X', 'Y']
		X, y, error = cleanRawXY(userInput.raw_x, userInput.raw_y)
	else:
		error = "Need both X and Y data"

	if error:
		print "error: %r" % error
		# Delete error entry from db
		userInput.delete()
		return render_to_response('mltest/error.html', 
			{'error': error}, context)
	else:
		# Build data array
		data = []
		for i in range(0, len(X)):
			row = []
			for j in range(0, len(X[0])):
				row.append(X[i][j])
			row.append(y[i])
			data.append(row)

		# Gradient descent
		n = len(X[0]) + 1   # +1 for bias column
		theta = [0.0] * n
		alpha = 0.1
		numIters = 500
		theta, J_history, mu, sigma = gradientDescent(X, y, 
			theta, alpha, numIters)

		# Check for undefined theta values
		for th in theta:
			if np.isnan(th):
				return render_to_response('mltest/error.html', 
				{'error': "Theta NaN"}, context)

		# Set up predict form fields
		predictForm = PredictForm(request.POST or None, n=n)		

		context_dict = {
			'id': inputId,
			'headers': tblHeaders,
			'data': data,
			'n': n,
			'theta': theta,
			'J': J_history[-11:-1],
			'mu': mu,
			'sigma': sigma,
			'predictForm': predictForm,
		}

	return render_to_response('mltest/results.html', context_dict, 
		context)

def cleanRawXY(raw_x, raw_y):
	X, y, error = [None, None, None]

	raw_x = raw_x.strip().strip(',')
	raw_y = raw_y.strip().strip(',')

	# Check for characters other than numbers and commas
	allowedChars = set('0123456789,.- ')
	if (any((char not in allowedChars) for char in raw_x) or
		any((char not in allowedChars) for char in raw_y)):
		error = "Contain character(s) other than number, comma, dash or period"
	else:
		try:
			X = [[float(val)] for val in raw_x.split(',')]
			y = [float(val) for val in raw_y.split(',')]

			# Trim arrays to the smallest size
			shortest = min(len(X), len(y))
			if shortest <= 1:
				error = "Need more than 1 point to plot"
			else:
				del X[shortest:]
				del y[shortest:]
		except Exception, e:
			error = e
	
	return [X, y, error]

def cleanRawFile(raw_file, filename):
	X, y, tblHeaders, error = [[], [], None, None]
	
	if mimetypes.guess_type(filename)[0] == 'text/csv':
		path = os.path.join("media", str(raw_file))
		with open(path, "rU") as inputFile:
			rowCount = 0
			rdr = csv.reader(inputFile)

			tblHeaders = rdr.next()
			numCols = len(tblHeaders)
			
			for row in rdr:
				if len(row) != numCols:
					error = "Row dimension mismatch (%d)" % numCols
					break
				try:
					row = [float(elem) for elem in row]
					X.append(row[0:-1])
					y.append(row[-1])
				except Exception, e:
					error = e
					break
				rowCount += 1
				if rowCount > 100:
					break
	else:
		error = "Invalid input file type (.csv only)"
			
	return [X, y, tblHeaders, error]
