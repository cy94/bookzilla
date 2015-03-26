// register.js

$(document).ready(function(){

	$('#password, #confirmpassword').focusout(function(){
		// both passwords must be the same
		if($('#password').find('input').val() != $('#confirmpassword').find('input').val()){
			$('#password, #confirmpassword').removeClass('has-success');
			$('#password, #confirmpassword').addClass('has-error');
		}
		else{
			$('#password, #confirmpassword').removeClass('has-error');
			$('#password, #confirmpassword').addClass('has-success');
		}
	});

	$('#register-form').on('submit', function(event){
		event.preventDefault();
		console.log('Register form submitted.');

		// check - 
		// all fields non-empty
		// passwords equal
		// raise errors

	    var $form = $(this);

	    // post to register_validate view - check if username and email taken
		$.post($(location).attr("href") + "register_validate", $form.serializeArray(), 
															   function(msg){
			console.log(msg);

			if(msg == "name_taken"){
				console.log("name is taken");
			}
			else if(msg == "email_taken"){
				console.log("email is taken");
			}
			else if(msg == "no_error"){
				console.log("all info ok, redirecting");
				// redirect to home
				window.location.href = '/users/home';
			}

			return false;
		});
	});
})