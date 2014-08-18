var AutoFill = function(xId, yId, bgId) {
	this.xInput = $(xId);
	this.yInput = $(yId);
	this.btnGrp = $(bgId);

	this.init();	// Lets initialize it
}

AutoFill.prototype.init = function() {
	var self = this;	
	var files = $(Data.files);

	// Create buttons in button group
	this.createBtns();
}

AutoFill.prototype.createBtns = function() {
	var self = this;
	var files = $(Data.files);
	var dsId, button, file;

	for (var i = 0; i < files.size(); i++) {
		file = files.get(i);
		dsId = i + 1;

		this.btnGrp.append('<button id="' + 'ds' + dsId + 
			'" type="button" class="btn btn-default">Dataset ' + dsId + '</button>');

		button = $('#ds' + dsId);

		// Set tooltip
		button.tooltip({
			container: 'body',
			title: file.description,
			placement: 'right'
		});		

		// Set click listener
		button.on("click", {filename: file.filename}, function(event) {	

			$.get('/static/mltest/Datasets/' + event.data.filename, function(data) {					
				Papa.parse(data, {
					download: false,				
					worker: true,
					complete: function(results) {
						var data = results.data;
						var x = new Array(), y = new Array();						

						for (var i = 1; i < data.length; i++) {
							x.push(data[i][0]);
							y.push(data[i][1]);
						};						
						self.xInput.val(x.join(", "));
						self.yInput.val(y.join(", "));
					}
				});
			});

		});

	};
};