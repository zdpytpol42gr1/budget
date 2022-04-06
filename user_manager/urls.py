from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.SignUpView.as_view(), name="register"),
    path("hi/", views.HiPageView.as_view(), name="hi_page"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("user_list/", views.UserListView.as_view(), name="user_list"),
    path("change_password/", views.ResetPasswordView.as_view(), name="change_password"),
]
