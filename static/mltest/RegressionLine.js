var RegressionLine = function(theta, mu, sigma, max) {

	this.theta = theta;
	this.mu = mu[0];
	this.sigma = sigma[0];
	this.max = max;
	this.regLine = [];
};

RegressionLine.prototype.create = function() {

	var norm_x = (this.max - this.mu) / this.sigma;	// Normalized x

	this.regLine.push([0, 0]);
	this.regLine.push([this.max, (this.theta[0] + this.theta[1] * norm_x)]);

	return this.regLine;
};