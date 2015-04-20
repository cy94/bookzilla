$(document).ready(function() {
	// confirm deletion of book 
	$('.delete-button').click(function(event){
		return confirm('Are you sure you want to remove this book?');
	});
});