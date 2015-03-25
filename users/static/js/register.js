// register.js

$(document).ready(function(){
	$('#register-form').on('submit', function(event){
		event.preventDefault();
		console.log('register form submitted');
	});
})