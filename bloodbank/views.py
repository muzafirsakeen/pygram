from typing import Text
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Userinfo

from django.contrib.auth.models import User,auth
# from .templates import bloodbank

# Create your views here.
# def blood(request):
#         return render(request,'login.html')

    
list1 = []

def add_donor(request):
    # if request.method=='POST':
    #     username = request.POST['your_name']
    #     bgroup = request.POST['bgroup']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    
    #     list1.append({'nme':username,'bdgrp':bgroup,'email':email,'phone':phone})


    #     # dicts= {'nme':[],'bdgrp':[],'email':[],'phone':[]}
    #     # dicts["nme"].append(username)
    #     # dicts["bdgrp"].append(bgroup)
    #     # dicts["email"].append(email)	
    #     # dicts["phone"].append(phone)
    #     return render(request,'bloodbank.html')
    # else:
    #     return render(request,'bloodbank.html')



    user=request.session.get('username')
    if request.method == 'POST':
        name = (request.POST['your_name'])
        blood_group = (request.POST['bgroup'])
        phone = (request.POST['phone'])
        email = (request.POST['email'])
        users = Userinfo.objects.create(name=name,blood_group=blood_group,phone_number=phone,email=email)
        return redirect(display)
    elif(user):
        user=request.session.get('username')
        return render(request,'bloodbank.html',{'user':user})
    else:
        return redirect("/")





     
def display(request):   
    
    user = request.session.get('username')   
    if(user):
        
        data = Userinfo.objects.all()
        return render(request,"bdres.html",{'data':data,'user':user})
    else:
        return redirect("/")



    # return render(request,'bdres.html',{'list1':list1})


list2 = []    
list3 =[]
# def signuup(request):
#     if request.method=='POST':
#         uname = request.POST['usname']
#         eml = request.POST['eail']
#         pass1 = request.POST['psw']
#         pass2 = request.POST['pscon']

#         if (pass1 == pass2):
#             if User.objects.filter(username = uname).exists():
#                 print("already exist")
#             else:
#                 user = User.object.create_user(uname = uname,password = pass1,email = eml)
#                 user.save()
#                 print ('user created')
#                 return redirect('/')
        
#         # if pass1 == pass2:
        #     list2.append({'uname':uname,'eml':eml,'pass1':pass1,})
        #     print (list2)
        #     return render(request,'login.html')
        # elif not uname or not eml or not pass1 or not pass2:

        #     return render(request,'signup.html')
        # else:
        #     return render(request,'signup.html')



    
        

def login(request):

    user = request.session.get('usern')

    if request.method =='POST':
        
        username = request.POST['usern']
        password = request.POST['password']
        # return render(request,'bloodbank.html')

        user  = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request, user)
            request.session['id'] = user.id
            request.session['username'] = user.username
            return render(request,'bres.html',{"name":username})
        else:
            messages.info(request,'Invalid Credentials..!')
            return redirect('login')
                    
    else:
        return render(request,'login.html')


       #-----------------------------------------------------------
       # with variable 
        # usern = request.POST['usern']
        # psw = request.POST['pswd']

        # for x in list2:
        #     varx= list2[0]['uname']
        #     vary = list2[0]['pass1']
            

        #     if varx == usern and vary == psw:
        #         return render(request,'bloodbank.html',{"name":varx})
        #     else:
        #         return render(request,'bloodbank.html')
                    
                



# def signp(request):
#     



# def signuup(request):
#     if request.method=='POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']

#         user = User.object.create_user(username = username,password = password1,email = email,first_name = first_name,last_name = last_name)
#         user.save()
#         print ('user created')
#         return redirect('/')


def signuup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['uname']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        email = request.POST['eail']

        if password1 == password2:

            if User.objects.filter(email = email).exists():
                messages.info(request,'Email Already exists')
                print("Email Already exist")
                return redirect('signuup')
            elif User.objects.filter(username = username).exists():

                messages.info(request,'Username Already Taken')
                print("User Name already taken")
                return redirect('signuup') 
            
            else:
                user = User.objects.create_user(username = username,password = password1,email = email,first_name = first_name,last_name = last_name)
                user.save()
                print('user created')
        else:
            print("password not matching")
            messages.info(request,'Password not matching...!')
        return redirect('/signuup/')
    else:
        return render(request,'signup.html')


def logout(request):
    return redirect("/")