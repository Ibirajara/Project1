from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UserExtendForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserEmpresaForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['empresa']
        
