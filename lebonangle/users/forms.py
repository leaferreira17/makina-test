from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=500)

    class Meta:
        model = MyUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "address",
            "password1",
            "password2",
        )
