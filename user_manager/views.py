from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import NewUserForm, LoginForm


def hi_page_view(request):
    return render(request, 'user_manager/hi_page.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect(hi_page_view)
    else:
        form = NewUserForm()
        if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect(login_page)

        return render(request, 'user_manager/register.html', {'form': form})


def login_page(request):
    if request.user.is_authenticated:
        return redirect(hi_page_view)
    else:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            form.save()

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(hi_page_view)
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'user_manager/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(hi_page_view)
