$(document).ready(function() {
	// confirm deletion of book 
	$('.done-button').click(function(event){
		return confirm('Please confirm that you have picked up/dropped off this book');
	});
});