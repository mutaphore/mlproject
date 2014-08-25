var RegressionLine = function(theta, mu, sigma, xRange, yRange) {
	this.theta = theta;
	this.mu = mu[0];
	this.sigma = sigma[0];
	this.xRange = xRange;
	this.yRange = yRange;
	this.regLine = [];
};

RegressionLine.prototype.create = function() {
	
	// We just need 2 points to plot the line
	var norm_x1 = (this.xRange[0] - this.mu) / this.sigma;
	var norm_x2 = (this.xRange[1] - this.mu) / this.sigma;		
	this.regLine.push([this.xRange[0], this.theta[0] + this.theta[1] * norm_x1]);
	this.regLine.push([this.xRange[1], this.theta[0] + this.theta[1] * norm_x2]);

	return this.regLine;
};