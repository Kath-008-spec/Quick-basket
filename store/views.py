# Create your views here.
# used to render HTML templates 

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import CustomSignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def test_view(request):
    """Simple test view to check if Django is working"""
    return HttpResponse("Django is working! QuickBasket is running.")

def product_view(request):
    products = Product.objects.all()
    return render(request, 'store/product.html', {'products': products})

def home_view(request):
    try:
        products = Product.objects.all()[:4]  # Get first 4 products for featured section
    except Exception as e:
        # If there's any database error, just use empty list
        products = []
    
    return render(request, 'store/home.html', {'products': products})

def signup_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after successful registration
            login(request, user)
            messages.success(request, f'Welcome to QuickBasket, {user.first_name}! Your account has been created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomSignUpForm()
    
    return render(request, 'store/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')
