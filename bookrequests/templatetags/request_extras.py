# template tags used for book requests

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

def show_request_owner(request):
	pass

# request tracking by the borrower of a book
def show_request_borrower(request):
	pass