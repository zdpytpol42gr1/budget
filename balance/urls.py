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
    IncomeCategoryDeleteView,
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
]
