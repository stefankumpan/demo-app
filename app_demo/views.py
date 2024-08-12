from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to the dashboard page
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def logout(request):
    if not request.user.is_authenticated:
        # Redirect to the login page after logging out
        return redirect('login')

    auth_logout(request)
    return redirect('home')  # Redirect to the home page after logging out


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page if not logged in
    # Add your dashboard logic here
    return render(request, 'dashboard.html')
