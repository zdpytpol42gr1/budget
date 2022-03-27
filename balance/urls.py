from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('balance/', views.balance_view, name='balance'),
    path('incomes/', views.incomes_view, name='incomes'),
    path('expenses/', views.expenses_view, name='expenses'),
]