from django.urls import path

from .views import ExpenseListView, ExpenseDetailView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, \
    ExpenseCategoryListView, ExpenseCategoryDetailView, ExpenseCategoryCreateView, ExpenseCategoryDeleteView

urlpatterns = [
    path('expense-list/', ExpenseListView.as_view(), name='expense_list'),
    path('expense-detail/<int:pk>', ExpenseDetailView.as_view(), name='expense_detail'),
    path('expense-create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('expense-update/<int:pk>', ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense-delete/<int:pk>', ExpenseDeleteView.as_view(), name='expense_delete'),

    path('category-list/', ExpenseCategoryListView.as_view(), name='expense_category_list'),
    path('category-detail/<int:pk>', ExpenseCategoryDetailView.as_view(), name='expense_category_detail'),
    path('category-create/', ExpenseCategoryCreateView.as_view(), name='expense_category_create'),
    path('category-delete/<int:pk>', ExpenseCategoryDeleteView.as_view(), name='expense_category_delete'),
]
