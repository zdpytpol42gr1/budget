from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import LoginForm, PasswordChangingForm
from django.views.generic import View
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView


class BaseView(View):
    template_name = "user_manager/base_view.html"

    def get(self, request):
        return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class ResetPasswordView(View):
    template_name = "user_manager/forgot-password.html"
    success_url = reverse_lazy("dashboard")
    form_class = PasswordChangingForm

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
            return redirect("dashboard")
        else:
            messages.error(request, "Please correct the error below.")
        form = PasswordChangeForm(request.user)
        return render(request, "user_manager/forgot-password.html", {"form": form})


class LoginPageView(View):
    template_name = "user_manager/login.html"
    form_class = LoginForm

    def get(self, request):

        if self.request.user.is_authenticated:
            return redirect("dashboard")
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
                return redirect("dashboard")
        message = "Login failed!"
        return render(
            request, self.template_name, context={"form": form, "message": message}
        )


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "user_manager/register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

