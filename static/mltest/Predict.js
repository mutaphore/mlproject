var Predict = function(n, theta, mu, sigma) {
	var y = theta[0];

	// Note: n includes bias
	for (var i = 1; i < n; i++) {
		var xVal = $.trim($("#X" + i).val());

		if (xVal.length > 0 && $.isNumeric(xVal)) {	
			y += ((xVal - mu[i-1]) / sigma[i-1]) * theta[i]
		}
		else
			return null;
	};	

	// Round to 3 decimal places
	return Math.round(y * 1000) / 1000;
}