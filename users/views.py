from django.contrib import auth
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_view(request):

    if request.user.is_authenticated:
        login(request,request.user)
        return redirect('/home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(username=username,password=password)


        if user is not None:
            login(request , user)
            return redirect('/home')

        else:
            messages.info(request , "Wrong username or password!!")
    return render(request , 'login.html')


def register_view(request):

    if request.method == 'GET':
        x,y = generate_captcha()

        context = {
            'x' : x,
            'y' : y,
        }

    if request.method == "POST":
        firstname = request.POST.get('first-name')
        lastname = request.POST.get('last-name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm-password')
        xvalue = request.POST.get('xvalue')
        yvalue = request.POST.get('yvalue')
        ans = request.POST.get('ans')

        
        if User.objects.filter(username=username).exists():
            messages.info(request , "User already exists!!")

        else:

            if password == confirm:
                if password.isalnum() and len(password)>=8 :
        
                    if int(ans) == int(xvalue) + int(yvalue):
            
                        messages.success(request , "User is registered successfully!!")

                        user = User.objects.create(first_name = firstname , last_name = lastname , email = email ,username = username)
                        user.set_password(password)
                        user.save()

                        login(request, user)

                        return redirect('/home')

                    else:
                        messages.info(request , "Captcha failed!!!!!!!!!!")

                else:
                    messages.info(request , "Password should be alphanumeric and 8 characters long")

            else:
                messages.info(request , "Password did't match!!!")

                  
        x,y = generate_captcha()

        context = {
        'x' : x,
        'y' : y,
        }  

    return render(request, 'register.html' , context)


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
def home_view(request):

    context = {
        'user' : request.user
    }

    if request.method == "POST":
        username = request.POST['username']

        user = User.objects.get(username = username)

        return redirect(f'/detail/{user.id}')

    return render(request , 'home.html' , context)

@login_required(login_url='/')
def edit_view(request):

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user = User.objects.get(username = request.user)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()

        context = {
        'user' : user
        }

        messages.info(request , "Changes Saved successfully!!!!")


        return render(request , 'home.html' , context)

    return render(request , 'home.html')

@login_required(login_url='/')
def detail_view(request , pk):

    user = User.objects.get(id = pk)

    context = {
        'user' : user
    }

    if request.method == "POST":
        username = request.POST['username']

        user = User.objects.get(username = username)

        if user == request.user:
            return redirect('/home')

        context = {
            'user': user
        }
    return render(request, 'detail.html' , context)

    



def generate_captcha():
    x = random.randint(0,30)
    y = random.randint(0,30)

    return x,y