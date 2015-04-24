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
		 "{0} sent you a request for {1}".format(borrower, title),
		BookRequest.REQUEST_ACCEPTED:
		 "Accepted request by {0} for {1}".format(borrower, title),
		BookRequest.REQUEST_REJECTED:
		 "Rejected request by {0} for {1}".format(borrower, title),
	}

	if req.status == BookRequest.REQUEST_MADE:
		accept_buttons = True

	print accept_buttons

	return {
		'request_id': req.id,
		'message': messages[req.status],
		'accept_buttons': accept_buttons
	}

# request tracking by the borrower of a book
@register.inclusion_tag('bookrequests/request_borrower.html')
def show_request_borrower(req):
	pass