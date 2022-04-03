from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import LoginForm
from django.views.generic import View, ListView, TemplateView
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView


class HiPageView(TemplateView):
    template_name = "user_manager/hi_page.html"


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("hi_page")


class UserListView(ListView):
    model = User
    template_name = "user_manager/user_list.html"


class ResetPasswordView(View):
    template_name = "user_manager/change_password.html"
    success_url = reverse_lazy("hi_page")
    form_class = PasswordChangeForm

    def get(self, request):
        form = self.form_class(User)
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("hi_page")
        else:
            messages.error(request, "Please correct the error below.")
        form = PasswordChangeForm(request.user)
        return render(request, "user_manager/change_password.html", {"form": form})


class LoginPageView(View):
    template_name = "user_manager/login.html"
    form_class = LoginForm

    def get(self, request):

        if self.request.user.is_authenticated:
            return redirect("hi_page")
        form = self.form_class()
        message = ""
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("hi_page")
        message = "Login failed!"
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "user_manager/register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"
