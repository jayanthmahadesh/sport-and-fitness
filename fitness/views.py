from django.shortcuts import render, redirect
from django.views import  View
from .models.user import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username_tobe_check = request.POST.get('username')
        password_tobe_check = request.POST.get('password')

        username_actual = User.objects.get(username = username_tobe_check)

        if username_actual:
            flag = check_password(password_tobe_check, username_actual.password)

            if flag:
                return redirect('indexpage')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')

        # if(password.length)



class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        error_message = None
        try:
            username = request.POST.get('usernameS')
            password = request.POST.get('passwordS')

            username_db = User.objects.get(username = username)

            if username_db:
                error_message = "email already exists"
                print(error_message)
                data = {
                    'error_message': error_message
                }
                return render(request, 'signup.html', data)

            if len(password) < 7:
                error_message = "password too short"
                data = {
                    'error_message' : error_message
                }
                return render(request, 'signup.html',data)
            else:
                user = User(username=username, password=password)
                print("username:-" + username)
                user.password = make_password(password)
                user.save()
                return redirect('indexpage')

        except:
            return render(request, 'signup.html')


class Index(View):
    def get(self,request):
        return render(request,'index.html')

class outdoor(View):
    def get(self,request):
        return render(request,'outdoor.html')
    