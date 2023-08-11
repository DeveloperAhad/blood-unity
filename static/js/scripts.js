(function($){
	jQuery(document).ready(function() {	

		// Scroll to Top
		jQuery('.scrolltotop').click(function(){
			jQuery('html').animate({'scrollTop' : '0px'}, 400);
			return false;
		});
		
		jQuery(window).scroll(function(){
			var upto = jQuery(window).scrollTop();
			if(upto > 500) {
				jQuery('.scrolltotop').fadeIn();
			} else {
				jQuery('.scrolltotop').fadeOut();
			}
		});

		jQuery(".menu-item2 ul li a").click(function() {
			jQuery(this).next().slideToggle();
		});

		$(".toggle-password").click(function() {

		  	$(this).toggleClass("fa-eye fa-eye-slash");
		  	var input = $($(this).attr("toggle"));
		  	if (input.attr("type") == "password") {
		    	input.attr("type", "text");
		  	} else {
		    	input.attr("type", "password");
		  }
		});


		

				
		
		
		
		
		
		
		
		
	});
})(jQuery);