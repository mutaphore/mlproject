var AutoFill = function(xId, yId, bgId) {
	this.xInput = $(xId);
	this.yInput = $(yId);
	this.btnGrp = $(bgId);
	this.datasets = [];
}

AutoFill.prototype.init = function() {
	var self = this;	
	var files = $(Data.files);

	// Create buttons in button group
	this.btnArr = createBtns(this.btnGrp);

	// Parse data
	$.each(files, function(index, file) {
		$.get('/static/mltest/Datasets/' + file.filename, function(data) {					
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
					self.datasets.push({x: x, y: y});													

					var button = $("#ds" + (index + 1));
					// Set click listener
					button.click(function() {
						self.xInput.val(self.datasets[index].x.join(", "));
						self.yInput.val(self.datasets[index].y.join(", "));
					});
					// Set tooltip
					button.tooltip({
						container: "body",
						title: file.description,
						placement: "right"
					})
				}
			});
		});	 
	});

	return this.datasets;
}

var createBtns = function(btnGrp) {
	var files = $(Data.files);

	for (var i = 0; i < Data.files.length; i++) {
		btnGrp.append('<button id="' + 'ds' + (i + 1) + 
			'" type="button" class="btn btn-default">Dataset ' + 
			(i + 1) +'</button>');
	};
}