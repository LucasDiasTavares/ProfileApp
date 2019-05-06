from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Herdo o meu UserCreationForm
class UserRegisterForm(UserCreationForm):
    # campos adicionais que quero adicionar
    email = forms.EmailField()

    # Referencio a qual model eu quero adicionar os campos
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

