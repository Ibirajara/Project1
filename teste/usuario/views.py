from django.shortcuts import render
from .forms import UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def login(request):
    model = User
    form = UserCreationForm
    

