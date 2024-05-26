"""
URL configuration for rentify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# rentify/urls.py
from django.contrib import admin
from django.urls import path, include  # Ensure 'include' is imported
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Include URLs from the 'main' app
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('seller/', views.seller_dashboard, name='seller_dashboard'),
    path('buyer/', views.buyer_dashboard, name='buyer_dashboard'),
]
