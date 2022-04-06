from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('home/', views.first_page, name='menu'),
    path('balance/', views.balance_view, name='balance'),
]
