from django import forms
from django.contrib.auth.forms import AuthenticationForm

from core.forms import StyledFormMixin


class LoginForm(StyledFormMixin, AuthenticationForm):
    username = forms.CharField(
        max_length=100,
    )
