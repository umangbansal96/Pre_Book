from django.shortcuts import render, redirect
from django.http import HttpResponse
#from service.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from servive.models import Contact


def home(request):
    if request.method == "POST":
        name = request.POST.get('txtName') 
        email = request.POST.get('txtEmail') 
        number = request.POST.get('txtPhone') 
        message = request.POST.get('txtMsg') 
        contact = Contact(name = name, email = email, number = number, message= message)
        contact.save()
    return render(request, "home.html")

def discription(request):
    return render(request, "discription.html")

def name(request):
    return render(request, "name.html")

def seatmap(request):
    return render(request, "seatmap.html")

def test(request):
    return render(request, "test.html")


def login(request):
    if request.method == "POST":
            username = request.POST.get('username')
            pass1 = request.POST.get('pass1')
            user = authenticate(username=username, password=pass1)
            
            if user is not None:
                login(request, user)  
                return render(request, "home.html")
            else:
                return HttpResponse('User not found')            
    return render(request, "login.html")


def signUp(request):
    if request.method=="POST":        
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            my_user = User.objects.create_user(username, email, password)
            my_user.save()            
            return redirect('login')     
    return render(request, 'signup.html')