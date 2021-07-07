from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='newpost'),
    path('view/<int:pk>/',views.view, name='viewpost'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register')
]