# contains forms needed for creating, editing a book
# and other functions

from django import forms

class EditBookForm(forms.Form):
	title = forms.CharField(label='Title')
	author = forms.CharField(label='Author')