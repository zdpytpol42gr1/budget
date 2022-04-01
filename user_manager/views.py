from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
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


@staff_member_required()
def del_user(request, username):
    u = User.objects.get(username=username)
    if request.method == 'POST':
        try:
            u.delete()
            return redirect(user_list_view)

        except User.DoesNotExist:
            messages.error(request, "User does not exist")
            return render(request, 'user_manager/accept.html')

        except Exception as e:
            return render(request, 'user_manager/accept.html', {'err': e.message})

    return render(request, 'user_manager/accept.html', {'user': u})


@staff_member_required()
def user_list_view(request):
    users = User.objects.all()

    return render(request, 'user_manager/user_list.html', {'users': users})


@login_required()
def change_password_by_user(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(hi_page_view)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user_manager/change_password.html', {'form': form})
