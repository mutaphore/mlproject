var Plot = function(data, theta, mu, sigma, id) {

	this.data = data;
	this.theta = theta;
	this.mu = mu;
	this.sigma = sigma;
	this.id = id;
	this.plot = null;
}

Plot.prototype.init = function() {

	var max = Math.max.apply(Math, 
		this.data.map(function(v) {return v[0];} ));
	var min = Math.min.apply(Math, 
		this.data.map(function(v) {return v[0];} ));
	var regLine = new RegressionLine(this.theta, 
		this.mu, this.sigma, min, max).create();

	var dataset = [
		{
			label: "Data",
			data: this.data,
			color: "#058DC7",
			points: {
                radius: 4,
                show: true,
                fill: true,
                fillColor:"#058DC7"
            }
		}, {
			label: "Regression Line",
			data: regLine,
			color: "#FF0000",
			lines: {show: true}
		}
	];

	var options = {
        axisLabels: {
            show: true
        },
        xaxes: [{
            axisLabel: 'X',
        }],
        yaxes: [{
            axisLabel: 'Y',
        }],
        legend: {
        	position: "se"
        }
	};

	// Plot it!
	this.plot = $.plot($("#" + this.id), 
		dataset, options);

	return this.plot;
}