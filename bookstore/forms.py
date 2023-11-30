from django import forms

class BookSearchForm(forms.Form):
    title = forms.CharField(label='Book Title', max_length=100)