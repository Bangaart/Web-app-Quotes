from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUser(UserCreationForm):
    username = forms.CharField(max_length=50, label='Username', widget=forms.TextInput())
    password1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=50, label='Password confirmation', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# class LoginUser(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
