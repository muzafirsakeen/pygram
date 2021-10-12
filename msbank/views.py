from typing import Text
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth

# Create your views here.
def signuup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.object.create_user(username = username,password = password1,email = email,first_name = first_name,last_name = last_name)
        user.save()
        print ('user created')
        return redirect('/')