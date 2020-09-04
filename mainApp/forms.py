from django import forms
from django.utils.encoding import smart_text
from django.forms.widgets import PasswordInput, TextInput, Textarea, EmailInput

class EmailForm(forms.Form):
    name = forms.CharField(max_length=20,  widget=TextInput(attrs={'placeholder': 'John Doe', 'rows': '3'}))
    email = forms.CharField(max_length=20,  widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'jdoe@gmail.com',  'rows': '3'}))
    subject = forms.CharField(max_length=50,  widget=TextInput(attrs={'placeholder': 'Exciting Oppurtunity',  'rows': '3'}))
    Message = forms.CharField(max_length=1000, widget=Textarea(attrs={'placeholder': 'Come work for me!'}))