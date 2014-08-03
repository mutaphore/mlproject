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

		if form.is_valid():
			userInput = form.save(commit=False)

			if request.FILES.get('raw_file'):
				userInput.raw_file = request.FILES['raw_file']

			userInput.save()
			return HttpResponseRedirect('results/' 
				+ str(userInput.id) + '/')
		else:
			print form.errors
	else:
		form = InputForm() # Display form

	context_dict = {
		'inputForm': form,
	}
	return render_to_response('mltest/index.html', context_dict, context)

def resultsView(request, inputId):
	context = RequestContext(request)

	userInput = Input.objects.get(id=inputId)
	data = []
	X = []
	y = []
	headers = []
	errors = []

	if userInput.raw_file: 

		if mimetypes.guess_type(userInput.filename())[0] == 'text/csv':

			path = os.path.join("media", str(userInput.raw_file))

			with open(path, "rU") as inputFile:
				rowCount = 0
				rdr = csv.reader(inputFile)
				headers = rdr.next()

				for row in rdr:
					# Only show the first 100 rows
					if rowCount > 100:
						break
					rowCount += 1
					# Convert string literal to float
					row = [float(elem) for elem in row]
					data.append(row)
					X.append(row[0:-1])
					y.append(row[-1])

				# Do gradient descent
				n = len(X[0]) + 1    # +1 for column of 1's
				theta = [0.0] * n
				alpha = 0.1
				numIters = 500
				gradientDescent(X, y, theta, alpha, numIters)
		else:
			errors.append("Invalid input file type (.csv only)")
	elif userInput.raw_x and userInput.raw_y:

		headers = ['x', 'y']
		X, y, error = clean(userInput.raw_x, userInput.raw_y)

		if error:
			errors.append(error)
		else:
			for i in range(0, min(len(X), len(y))):
				data.append((X[i][0], y[i][0]))

			# Do gradient descent				
			theta = [0.0, 0.0]
			alpha = 0.1
			numIters = 500
			gradientDescent(X, y, theta, alpha, numIters)
	else:
		errors.append("Need both X and Y data")

	context_dict = {
		'id': inputId,
		'headers': headers,
		'data': data,
		'errors': errors
	}

	return render_to_response('mltest/results.html', context_dict, context)

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

	return [X, y, error]

	