var RegressionLine = function(theta, mu, sigma, max) {

	this.theta = theta;
	this.mu = mu[0];
	this.sigma = sigma[0];
	this.max = max;
	this.regLine = [];
};

RegressionLine.prototype.create = function() {
	var norm_x1 = (0 - this.mu) / this.sigma;
	var norm_x2 = (this.max - this.mu) / this.sigma;

	this.regLine.push([0, (this.theta[0] + this.theta[1] * norm_x1)]);
	this.regLine.push([this.max, (this.theta[0] + this.theta[1] * norm_x2)]);

	return this.regLine;
};