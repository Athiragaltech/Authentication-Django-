# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register,login
from . import views

urlpatterns = [
    path('', register, name='register'),
    path('login/', login, name='login'),
   
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   
    path('index/', views.index, name='index'),
]

