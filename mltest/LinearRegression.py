import numpy as np

# X: 2D python list
# y: 1D python list
# theta: 1D python list
def gradientDescent(X, y, theta, alpha, numIters):
	X = featureNormalize(X)

	J_history = []
	n = len(theta)
	m = len(y)

	# Convert to numpy structures for easier matrix indexing
	ones = np.array([1.0] * m)
	ones.shape = (m, 1)
	X = np.concatenate((ones, X), axis=1)	# Add intercept term
	y = np.array(y)
	y.shape = (m, 1)
	theta = np.array(theta)

	# print ones
	# print X
	# print y
	# print theta

	for itr in range(0, numIters):
		temp = np.array([0.0] * n)
		for j in range(0, n):
			tot = 0.0;
			for i in range(0, m):
				x = X[i,:]
				h = hyp(x, theta)
				tot += (h - y[i]) * x[j]

			# Update thetas simultaneously
			temp[j] = theta[j] - alpha / m * tot

		theta = temp
		J_history.append(computeCost(X, y, theta))
	
	print "J: %r" % J_history[-1][0]
	for j in range(0, n):
		print "theta%d: %r" % (j, theta[j])

	return theta

def computeCost(X, y, theta):
	cost = 0
	m = len(y)

	for i in range(0, m):
		cost += (hyp(X[i], theta) - y[i])**2

	return cost / (2 * m)

def hyp(x, theta):
	theta_t = np.transpose(theta)
	h = np.dot(x, theta_t)
	return h

# X: 2D python list
def featureNormalize(X):
	X_norm = np.array(X)
	m = X_norm.shape[0]
	if X_norm.ndim > 1:
		n = X_norm.shape[1]
	else:
		n = 1

	mu = np.zeros((n, 1))
	sigma = np.zeros((n, 1))

	for j in range(0, n):
		mu[j] = np.mean(X_norm[:,j])
		sigma[j] = np.std(X_norm[:,j])

	for i in range(0, m):
		x = X_norm[i,:]
		X_norm[i,:] = np.divide(np.subtract(x, mu), sigma) 

	return X_norm