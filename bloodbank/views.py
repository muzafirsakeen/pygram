from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Userinfo
from django.http import JsonResponse



def user_login(request):
    user = request.session.get('username')
    if request.method == "POST":
        username  = request.POST['username']
        password  = request.POST['password']
        
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            request.session['id'] = user.id
            request.session['username'] = user.username

            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            return JsonResponse(
                {'success':False},
                safe=False
            )
    elif(user):
        return redirect('/display')
    else:
        return render(request,"login.html",{'user':user})


def signup(request):
        user=request.session.get('username')
        if request.method == "POST":
            first_name  = request.POST['first_name']
            last_name   = request.POST['last_name']
            username    = request.POST['username']
            email_id    = request.POST['email']
            password_1  = request.POST['pass1']
            password_2  = request.POST['pass2']

            if (password_1 == password_2):
                if User.objects.filter(username=username):
                    messages.info(request,'Username taken')
                    return redirect('/signup')
                elif User.objects.filter(email=email_id):
                   messages.info(request,'Email taken')
                   return redirect('/signup')
                else:
                   users = User.objects.create_user(username=username,password=password_1,email=email_id,first_name=first_name,last_name=last_name)
                   users.save()
                   return redirect('/')
               
            else:
                messages.info(request,'password not matching')
                return redirect(user_login)
            return redirect(signup)
        elif(user):
            return redirect('/display')
        else:
            return render(request,'signup.html',{'user':user})


def display(request):
    user = request.session.get('username')   
    if(user):
        
        data = Userinfo.objects.all()
        return render(request,"bdres.html",{'data':data,'user':user})
    else:
        return redirect("/")


def add_donor(request):
         
        user=request.session.get('username')
        if request.method == 'POST':
            name = (request.POST['your_name'])
            blood_group = (request.POST['blood_group'])
            phone = (request.POST['phone'])
            email = (request.POST['email'])


            users = Userinfo.objects.create(name=name,blood_group=blood_group,phone_number=phone,email =email)
            return redirect(display)

        elif(user):
            user=request.session.get('username')
            return render(request,'bloodbank.html',{'user':user})
        else:
            return redirect("/")


def logout(request):
    try:
        request.session.flush()
        
    except:
        pass
    return redirect("/")
