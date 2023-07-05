(function($){
	$.fn.bounceBox = function(){
		this.css({
			top			: -this.outerHeight(),
			marginLeft	: -this.outerWidth()/2,
			position	: 'absolute',
			left		: '0'
		});
		return this;
	}
	$.fn.bounceBoxShow = function(){
		this.stop().animate({top:0},{easing:'easeOutBounce'});
		this.data('bounceShown',true);
		return this;
	}
	$.fn.bounceBoxHide = function(){
		this.stop().animate({top:-this.outerHeight()});
		this.data('bounceShown',false);
		return this;
	}
	$.fn.bounceBoxToggle = function(){
		if(this.data('bounceShown'))
			this.bounceBoxHide();
		else
			this.bounceBoxShow();
		
		return this;
	}
})(jQuery);