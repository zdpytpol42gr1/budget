from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.SignUpView.as_view(), name="register"),
    path("index/", views.IndexView.as_view(), name="index"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("change_password/", views.ResetPasswordView.as_view(), name="change_password"),
]
