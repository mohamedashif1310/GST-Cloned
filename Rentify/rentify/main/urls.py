from django.urls import path
from .views import login_view, home_view
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_view, name='login'),
    #path('home/', home_view, name='home'),
]
