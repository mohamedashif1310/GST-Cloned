# main/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, PropertyForm
from .models import Property

def index(request):
    return render(request, 'main/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a new URL
        else:
            return render(request, 'main/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'main/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def seller_dashboard(request):
    if request.user.is_seller:
        properties = Property.objects.filter(user=request.user)
        return render(request, 'main/seller.html', {'properties': properties})
    else:
        return redirect('index')

def buyer_dashboard(request):
    if request.user.is_tenant:
        properties = Property.objects.all()
        return render(request, 'main/buyer.html', {'properties': properties})
    else:
        return redirect('index')
def home_view(request):
    return render(request, 'main/home.html')