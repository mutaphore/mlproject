var RegressionLine = function(theta, mu, sigma, range) {

	this.theta = $(theta);
	this.mu = mu[0];
	this.sigma = sigma[0];
	this.range = $(range);
	this.regLine = [];
};

RegressionLine.prototype.create = function() {

	// console.log(this.mu[0]);
	// console.log(this.sigma[0]);

	for (var i = this.range[0]; i < this.range[1]; i++) {
		var norm_x = (i - this.mu) / this.sigma;	// Normalized x
		var point = [i, (this.theta[0] + this.theta[1] * norm_x)];
		this.regLine.push(point);
	};

	return this.regLine;
};