# main/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Property

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2', 'is_tenant', 'is_seller')

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'city', 'place', 'nearby_schools', 'nearby_hospitals', 'no_of_bedrooms', 'no_of_bathrooms', 'price']
