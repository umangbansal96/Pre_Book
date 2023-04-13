from django.shortcuts import render, redirect
from django.http import HttpResponse
#from service.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



def login(request):
    if request.method == "POST":
            
            username = request.POST.get('username')
            pass1 = request.POST.get('pass1')
            user = authenticate(username=username, password=pass1)
            
            if user is not None:
                login(request, user)  
                return HttpResponse('Logged in successfully')
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