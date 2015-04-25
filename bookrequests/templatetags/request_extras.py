# template tags used for book requests

from bookrequests.models import BookRequest

from django import template

register = template.Library()

# request tracking by the owner of a book
# 1. accept/reject request
# 2. pending pickup
# 3. with courier, going to borrower
# 4. with borrower
# 5. borrower finished reading
# 6. with courier, coming back
# 7. completed

@register.inclusion_tag('bookrequests/request_owner.html')
def show_request_owner(req):
	accept_buttons = False

	borrower = str(req.borrower)
	title = str(req.book.title)
	author = str(req.book.author)

	messages = {
		BookRequest.REQUEST_MADE:
			 "{0} sent you a request for {1}",
		BookRequest.REQUEST_ACCEPTED:
			 "Accepted request by {0} for {1}",
		BookRequest.REQUEST_REJECTED:
			 "Rejected request by {0} for {1}",
		BookRequest.WITH_COURIER_TO_BORROWER:
			"Your book {1} is being sent to {0}", 
		BookRequest.WITH_BORROWER:
			"Your book {1} is with {0}", 
		BookRequest.DONE_READING:
			"{0} has finished reading your book {1}", 
		BookRequest.WITH_COURIER_TO_OWNER:
			"Your book {1} is being sent back to you from {0}", 
		BookRequest.RETURNED:
			"{1} has been returned by {0}", 
	}

	if req.status == BookRequest.REQUEST_MADE:
		accept_buttons = True

	print accept_buttons

	return {
		'request_id': req.id,
		# add the borrower and title into the message
		'message': messages[req.status].format(borrower, title),
		'accept_buttons': accept_buttons
	}

# request tracking by the borrower of a book
@register.inclusion_tag('bookrequests/request_borrower.html')
def show_request_borrower(req):
	pass

# request tracking by the courier
@register.inclusion_tag('bookrequests/request_courier.html')
def show_request_courier(req):
	pass	