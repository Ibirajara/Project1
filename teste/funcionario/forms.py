from django import forms
from funcionario.models import Funcionario

class FuncForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [ 'nome', 'cpf', 'telefone', 'cargo', 'nascimento', 'saldo', 'inativo', 'empresa' ]
        widgets = {'empresa': forms.HiddenInput() }