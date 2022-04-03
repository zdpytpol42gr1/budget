from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import NewUserForm


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="user_manager/register.html",
        context={"register_form": form},
    )
