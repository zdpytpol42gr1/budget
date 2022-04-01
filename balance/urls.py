from . import models
from django.urls import path, reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

urlpatterns = [
    # path('balance/', views.balance_view, name='balance'),
    # path('expenses/', views.expenses_view, name='expenses'),
    path('incomes/', ListView.as_view(model=models.Income), name='income_list'),
    path('income-add/', CreateView.as_view(model=models.Income, fields='__all__', success_url=reverse_lazy('income_list')), name='income_add'),
    path('income-detail/<int:pk>/', DetailView.as_view(model=models.Income, template_name='balance/income_detail.html'), name='income_detail'),
    path('income-edit/<int:pk>/', UpdateView.as_view(model=models.Income, fields='__all__', success_url=reverse_lazy('income_list')), name='income_edit'),
    path('income-delete/<int:pk>/', DeleteView.as_view(model=models.Income, success_url=reverse_lazy('income_list')), name='income_delete'),

    path('income-categories/', ListView.as_view(model=models.IncomeCategory), name='income_category_list'),
    path('income-category-add/', CreateView.as_view(model=models.IncomeCategory, fields='__all__', success_url=reverse_lazy('income_category_list')), name='income_category_add'),
    path('income-category-detail/<int:pk>/', DetailView.as_view(model=models.IncomeCategory, template_name='balance/income_category_detail.html'), name='income_category_detail'),
    path('income-category-edit/<int:pk>/', UpdateView.as_view(model=models.IncomeCategory, fields='__all__', success_url=reverse_lazy('income_category_list')), name='income_category_edit'),
    path('income-category-delete/<int:pk>/', DeleteView.as_view(model=models.IncomeCategory, success_url=reverse_lazy('income_list')), name='income_category_delete'),

]
