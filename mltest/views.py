import os
import csv
import mimetypes
import numpy as np

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from mltest.models import Input
from mltest.forms import InputForm
from mltest.LinearRegression import gradientDescent

def indexView(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = InputForm(request.POST, request.FILES)
		errors = []

		if form.is_valid():
			userInput = form.save(commit=False)
			userInput.raw_file = request.FILES.get('raw_file')

			if (userInput.raw_file or 
				(userInput.raw_x and userInput.raw_y)):
				userInput.save()
				request.session['inputId'] = userInput.id;
				return HttpResponseRedirect('results/')
			else:
				errors.append("Need both X and Y data")
		else:
			errors.append(form.errors)

		return render_to_response('mltest/error.html', 
			{'errors': errors}, context)

	else:  # Display form
		form = InputForm()
		return render_to_response('mltest/index.html', 
			{'inputForm': form}, context)

def resultsView(request):
	context = RequestContext(request)

	inputId = request.session.get('inputId')
	userInput = Input.objects.get(id=inputId)

	data = []
	errors = []

	if userInput.raw_file:

		if mimetypes.guess_type(userInput.filename())[0] == 'text/csv':

			path = os.path.join("media", str(userInput.raw_file))

			with open(path, "rU") as inputFile:
				rowCount = 0
				rdr = csv.reader(inputFile)

				headers = rdr.next()
				X = []
				y = []

				for row in rdr:
					# Only show the first 100 rows
					if rowCount > 100:
						break
					rowCount += 1
					# Convert string literal to float
					try:
						row = [float(elem) for elem in row]
						data.append(row)
						X.append(row[0:-1])
						y.append(row[-1])
					except Exception, e:
						errors.append(e)
		else:
			errors.append("Invalid input file type (.csv only)")
	elif userInput.raw_x and userInput.raw_y:

		headers = ['x', 'y']
		X, y, error = clean(userInput.raw_x, userInput.raw_y)

		if error:
			errors.append(error)
		else:
			# n = 2
			initTheta = [0.0, 0.0]
			for i in range(0, min(len(X), len(y))):
				data.append((X[i][0], y[i][0]))

	if errors:
		# Delete error entry from db
		userInput.delete()
		return render_to_response('mltest/error.html', 
			{'errors': errors}, context)
	else:
		# Do gradient descent
		n = len(X[0]) + 1   # +1 for bias column of 1's
		initTheta = [0.0] * n
		alpha = 0.1
		numIters = 500
		theta, J, mu, sigma = gradientDescent(X, y, initTheta, alpha, numIters)

		context_dict = {
			'id': inputId,
			'headers': headers,
			'data': data,
			'n': range(0, n),
			'theta': theta,
			'J': J[-11:-1],
			'mu': mu,
			'sigma': sigma,
		}
	return render_to_response('mltest/results.html', context_dict, 
		context)

def clean(raw_x, raw_y):
	X, y, error = [None, None, None]

	raw_x = raw_x.strip().strip(',')
	raw_y = raw_y.strip().strip(',')

	# Check for characters other than numbers and commas
	allowedChars = set('0123456789,. ')
	if (any((char not in allowedChars) for char in raw_x) or
		any((char not in allowedChars) for char in raw_y)):
		error = "Contain characters other than numbers, commas or periods"
	else:
		try:
			X = [[float(val)] for val in raw_x.split(',')]
			y = [[float(val)] for val in raw_y.split(',')]
		except Exception, e:
			error = e

	print X
	print y

	return [X, y, error]
