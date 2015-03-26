// register.js

$(document).ready(function(){
	$('#password, #confirmpassword').focusout(function(){
		if($(this).find('input').val().length == 0){
			$(this).removeClass('has-success');		
			$(this).addClass('has-error');	
		}
		else{
			$(this).removeClass('has-error');	
			$(this).addClass('has-success');		
		}

		if($('#password').find('input').val() != $('#confirmpassword').find('input').val()){
			$('#password, #confirmpassword').addClass('has-error');
		}
		else{
			$('#password, #confirmpassword').removeClass('has-error');
		}
	});

	$('#register-form').on('submit', function(event){
		event.preventDefault();
		console.log('register form submitted');

		$.ajax({
		    url : "register_validate/", // the endpoint
		    type : "POST", // http method
		    data : { the_post : $('#post-text').val() }, // data sent with the post request

		    // handle a successful response
		    success : function(json) {
		        $('#post-text').val(''); // remove the value from the input
		        console.log(json); // log the returned json to the console
		        console.log("success"); // another sanity check
		    },

		    // handle a non-successful response
		    error : function(xhr,errmsg,err) {
		        $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
		            " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
		        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		    }
		});

	});
})