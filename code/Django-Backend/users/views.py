from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Incorrect username or password"))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

# Create your views here.
    
def home(request):
    return render(request, 'authenticate/confirmation.html', {})
