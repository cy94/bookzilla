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

	if req.status == BookRequest.REQUEST_MADE:
		message = str(req.borrower) + \
				" sent you a request for " + \
				str(req.book.title) + \
				" (by " + str(req.book.author) + ")"

		accept_buttons = True

	return {
		'message': message,
		'accept_buttons': accept_buttons
	}

# request tracking by the borrower of a book
@register.inclusion_tag('bookrequests/request_borrower.html')
def show_request_borrower(req):
	pass