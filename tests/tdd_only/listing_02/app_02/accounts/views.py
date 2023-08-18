from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login as auth_login, logout as auth_logout
import uuid
import sys 
from accounts.models import Token 

def send_login_email(request):
    """-> send link for login to email""" 

    email = request.POST['email']
    uid = str(uuid.uuid4())
    token = Token.objects.create(email=email, uid=uid)
    print('saving uid', uid, 'for email', email, file=sys.stderr)
    url = request.build_absolute_uri(f'/accounts/login?uid={uid}')
    subject = 'Your login link for lists'
    body = f'Use this link to log-in -> \n\n{url}'
    from_email = 'noreply@superuser'
    to_list = [email,]
    send_mail(subject, body, from_email, to_list)
    messages.success(request, 'Link to enter send')
    return render(request, 'login_email_sent.html')


def login(request):
    """-> register in system""" 

    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')

def logout(request):
    """-> exit from system""" 

    auth_logout(request)
    return redirect('/')