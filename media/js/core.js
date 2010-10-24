var viva = function() {
	var init = function() {
		var self = this;
		
		$('#flak-shot').click(dismantle_flak);
	}
	
	var dismantle_flak = function() {
		$(".foo")
			.attr('target','_blank')
			.each(function() {window.open(this.href);})
	}

	return {
		init: init
	}
}();

$(document).ready(function() {
	viva.init();
});
