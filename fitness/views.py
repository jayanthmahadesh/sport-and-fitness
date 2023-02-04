from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth.hashers import make_password, check_password

from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.

def Login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            username_actual = custom_user.objects.get(email=email)
            try:
                if username_actual:
                    flag = check_password(password, username_actual.password)

                    if flag:
                        messages.success(request,'logged in successfully!')

                        request.session['username'] = username_actual.email
                        return redirect('indexpage')
                    else:
                        messages.error(request,'bad credentials')
                        return render(request, 'login.html')
            except:
                messages.error(request,'bad credentials')
                return render(request, 'login.html')
        except:
            messages.error(request,'bad credentials')
            return render(request, 'login.html')
    return render(request, 'login.html')


class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect('indexpage')
def SignUp(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        newuser = custom_user(email=email,password=password)
        newuser.password = make_password(password)
        newuser.save()
        messages.success(request,"your account has been created.")
        return redirect('login')
    return render(request,'signup.html')



def Index(request):
    # event = indoor_activities.objects.all()
    # print(event[0].bet)
    
    return render(request,'index.html')

def Indoor(request):
    event = indoor_activities.objects.all()
    print(event[0].event_image.url)
    return render(request,'indoor.html',{'event':event})

def outdoor(request):
    return render(request,'outdoor.html')

def timing(request):
    return render(request,'timing.html')

def timing_all(request):
    return render(request,'timing_all.html')

def Success(request):
    return render(request,'success.html')

def Success_Custom(request):
    return render(request,'success_custom.html')
def register(request):
    return render(request,'register.html')