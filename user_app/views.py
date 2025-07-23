from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserCreation
from .forms import CreateUserForm



def login_user(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username , password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'user_app/login.html')
    return render(request, 'user_app/login.html')

def register_user(request):
    if (request.method == 'POST'):
        frm = CreateUserForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('login')
        else:
            return render(request, 'user_app/register_user.html', {'form': frm})
    else:
        frm = CreateUserForm()
        return render(request, 'user_app/register_user.html', {'form': frm})

def logout_user(request):
    logout(request)
    return redirect('home')