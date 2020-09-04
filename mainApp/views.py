from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from mainApp.forms import EmailForm
import random, string
import json
import urllib
from django.conf import settings
import sys
import os
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse

from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required, user_passes_test

#user model for authentication
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.views.static import serve 



#Used for AJAX request, JsonResponse in manager.html, manager_vue.js
from django.http import JsonResponse


from django.views.decorators.csrf import csrf_exempt

#SMTP 
from django.core.mail import send_mail

#URL Validation
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
    # -*- coding: utf-8 -*-

def index(request):
    
    form = EmailForm()
    if request.method == 'POST':

        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['Message']
            recipient_list = ['receiver@gmail.com',]
            send_mail(
                                'New message from ' + name + ': ' + subject,
                                message + '\nSenders email: ' + email + '\nGenerated from Personal Portfolio Site',
                                    'bendfunk@gmail.com',
                                    ['bendfunk@gmail.com'],
                                    fail_silently=False,
                                    )
            return redirect('index')
        
            

    return render(request, 'index.html', {'form':form})