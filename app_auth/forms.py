from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    name = forms.CharField(max_length=30, label='Имя')
    surname = forms.CharField(max_length=30, label='Фамилия')
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'password']
