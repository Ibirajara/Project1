from django.forms import ModelForm
from .models import Empresa

class EmpresaForm(ModelForm):
    model = Empresa
    fields = ['nome', 'cnpj']