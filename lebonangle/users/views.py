from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import RegisterUserForm

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("item-list")
        else:
            messages.success(
                request,
                (
                    (
                        """Your email and/or password is wrong, please try again or register <a href="register">here</a>"""
                    )
                ),
            )
            return redirect("login_user")
    else:
        return render(request, "authentication/login.html", {})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration was successful"))
            return redirect("item-list")
        else:
            messages.success(
                request, ("There was an error with your registration... Please retry.")
            )
    else:
        form = RegisterUserForm()
    return render(request, "authentication/register.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, ("You logged out successfully !"))
    return redirect("item-list")
