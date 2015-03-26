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
			$('#password, #confirmpassword').addClass('has-success');
		}
	});

	$('#register-form').on('submit', function(event){
		event.preventDefault();
		console.log('Register form submitted.');


		var username = $('#username').val();
	    if (username == ''){
	       alert('Please enter your username !');
	       return false;
	    }

	    var $form = $(this);
		$.ajax({
			type: "POST",
			url: {% url 'users:register_validate' %},
			data: $form.serialize(),
			dataType: "json",
			success: function(response) {
				if (!response.success) {
	                alert(response.error);
	            }else {
		            alert('This username is available!');
	            }
			},
			error: function(rs, e) {
				alert(rs.responseText);
				return false;
			}
		}); 
	});
})