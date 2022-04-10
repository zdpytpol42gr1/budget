from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.SignUpView.as_view(), name="register"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("change_password/", views.ResetPasswordView.as_view(), name="change_password"),
    path("home/", views.BaseView.as_view(), name="home"),
]
