from django.urls import path

from balance import views

urlpatterns = [
    path("incomes/", views.IncomeListView.as_view(), name="income_list"),
    path("income-add/", views.IncomeCreateView.as_view(), name="income_add"),
    path(
        "income-detail/<int:pk>/",
        views.IncomeDetailView.as_view(),
        name="income_detail",
    ),
    path("income-edit/<int:pk>/", views.IncomeUpdateView.as_view(), name="income_edit"),
    path(
        "income-delete/<int:pk>/",
        views.IncomeDeleteView.as_view(),
        name="income_delete",
    ),
    path(
        "income-categories/",
        views.IncomeCategoryListView.as_view(),
        name="income_category_list",
    ),
    path(
        "income-category-add/",
        views.IncomeCategoryCreateView.as_view(),
        name="income_category_add",
    ),
    path(
        "income-category-detail/<int:pk>/",
        views.IncomeCategoryDetailView.as_view(),
        name="income_category_detail",
    ),
    path(
        "income-category-edit/<int:pk>/",
        views.IncomeCategoryUpdateView.as_view(),
        name="income_category_edit",
    ),
    path(
        "income-category-delete/<int:pk>/",
        views.IncomeCategoryDeleteView.as_view(),
        name="income_category_delete",
    ),
]
