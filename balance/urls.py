from django.urls import path, reverse_lazy
from .models import Expense, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('expense-list/', ListView.as_view(model=Expense), name='expense_list'),
    path('expense-detail/<int:pk>', DetailView.as_view(model=Expense), name='expense_detail'),
    path('expense-create/',
         CreateView.as_view(model=Expense, fields='__all__', success_url=reverse_lazy('expense_list')),
         name='expense_create'),
    path('expense-update/<int:pk>',
         UpdateView.as_view(model=Expense, fields='__all__', success_url=reverse_lazy('expense_list')),
         name='expense_update'),
    path('expense-delete/<int:pk>', DeleteView.as_view(model=Expense, success_url=reverse_lazy('expense_list')),
         name='expense_delete'),

    path('category-list/', ListView.as_view(model=Category), name='category_list'),
    path('category-detail/<int:pk>', DetailView.as_view(model=Category), name='category_detail'),
    path('category-create/',
         CreateView.as_view(model=Category, fields='__all__', success_url=reverse_lazy('category_list')),
         name='category_create'),
    path('category-delete/<int:pk>', DeleteView.as_view(model=Category, success_url=reverse_lazy('category_list')),
         name='category_delete'),
]
