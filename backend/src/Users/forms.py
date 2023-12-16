from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    # TODO: Custom authentication
    pass


class RegistrationForm(UserCreationForm):
    # TODO: Add custom validation
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
