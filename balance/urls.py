from django.urls import path

from .views import (
    IncomeListView,
    IncomeDetailView,
    IncomeCreateView,
    IncomeUpdateView,
    IncomeDeleteView,
    IncomeCategoryListView,
    IncomeCategoryDetailView,
    IncomeCategoryCreateView,
    IncomeCategoryDeleteView, ExpenseListView, ExpenseDetailView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, \
    ExpenseCategoryListView, ExpenseCategoryDetailView, ExpenseCategoryCreateView, ExpenseCategoryDeleteView, \
    ExpenseSummaryTemplateView, ExpenseCategoryUpdateView
)

urlpatterns = [
    path("income-list/", IncomeListView.as_view(), name="income_list"),
    path("income-detail/<int:pk>", IncomeDetailView.as_view(), name="income_detail"),
    path("income-create/", IncomeCreateView.as_view(), name="income_create"),
    path("income-update/<int:pk>", IncomeUpdateView.as_view(), name="income_update"),
    path("income-delete/<int:pk>", IncomeDeleteView.as_view(), name="income_delete"),
    path(
        "income-category-list/",
        IncomeCategoryListView.as_view(),
        name="income_category_list",
    ),
    path(
        "income-category-detail/<int:pk>",
        IncomeCategoryDetailView.as_view(),
        name="income_category_detail",
    ),
    path(
        "income-category-create/",
        IncomeCategoryCreateView.as_view(),
        name="income_category_create",
    ),
    path(
        "income-category-delete/<int:pk>",
        IncomeCategoryDeleteView.as_view(),
        name="income_category_delete",
    ),

    path('expense-list/', ExpenseListView.as_view(), name='expense_list'),
    path('expense-detail/<int:pk>', ExpenseDetailView.as_view(), name='expense_detail'),
    path('expense-create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('expense-update/<int:pk>', ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense-delete/<int:pk>', ExpenseDeleteView.as_view(), name='expense_delete'),

    path('category-list/', ExpenseCategoryListView.as_view(), name='expense_category_list'),
    path('category-detail/<int:pk>', ExpenseCategoryDetailView.as_view(), name='expense_category_detail'),
    path('category-create/', ExpenseCategoryCreateView.as_view(), name='expense_category_create'),
    path('category-update/<int:pk>', ExpenseCategoryUpdateView.as_view(), name='expense_category_update'),
    path('category-delete/<int:pk>', ExpenseCategoryDeleteView.as_view(), name='expense_category_delete'),
    path('expense-summary/', ExpenseSummaryTemplateView.as_view(), name='expense_summary'),

