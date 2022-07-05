from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('signup', views.signuphandle, name='signuphandle'),
    path('login', views.loginhandle, name='loginhandle'),
    path('logout', views.logouthandle, name='logouthandle'),
]
