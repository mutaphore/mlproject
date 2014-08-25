// Wrapper on the flot library to initialize a plot
var Plot = function(data, theta, mu, sigma, id) {

	this.data = data;
	this.theta = theta;
	this.mu = mu;
	this.sigma = sigma;
	this.id = "#" + id;
	this.plot = null;
}

Plot.prototype.init = function() {

	var xMax = Math.max.apply(Math, 
		this.data.map(function(v) {return v[0];} ));
	var xMin = Math.min.apply(Math, 
		this.data.map(function(v) {return v[0];} ));
	var yMax = Math.max.apply(Math, 
		this.data.map(function(v) {return v[1];} ));
	var yMin = Math.min.apply(Math, 
		this.data.map(function(v) {return v[1];} ));

	var regLine = new RegressionLine(this.theta, 
		this.mu, this.sigma, [xMin, xMax], [yMin, yMax]).create();

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
        grid: {
			hoverable: true,
			clickable: true
		},
        legend: {
        	position: "se"
        }
	};

	// Show tooltip with coordinate values
	$("<div id='tooltip'></div>").css({
		position: "absolute",
		display: "none",
		border: "1px solid #fdd",
		padding: "2px",
		"background-color": "#fee",
		opacity: 0.80
	}).appendTo("body");

	$(this.id).bind("plothover", function (event, pos, item) {
		var str = "(" + pos.x.toFixed(2) + ", " + pos.y.toFixed(2) + ")";
		$("#hoverdata").text(str);

		if (item) {
			var x = item.datapoint[0].toFixed(2),
				y = item.datapoint[1].toFixed(2);

			$("#tooltip").html("(" + x + ", " + y + ")")
				.css({top: item.pageY+5, left: item.pageX+5})
				.fadeIn(200);
		} else {
			$("#tooltip").hide();
		}
	});
	
	// Plot it!
	this.plot = $.plot($(this.id), 
		dataset, options);

	return this.plot;
}