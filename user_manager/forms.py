from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'class': "form-control"}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ["username", "email"]


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old password"),
                                   strip=False,
                                   widget=forms.PasswordInput(
                                   attrs={"autocomplete": "current-password", "autofocus": True, 'class': "form-control"}))

    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': "form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': "form-control"}))
