from django.forms import ModelForm
from funcionario.models import Funcionario


class FuncForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = [ 'nome', 'cpf', 'telefone', 'cargo', 'nascimento', 'saldo', 'inativo' ]
        


        #''', 'telefone',  'cargo', 'nascimento', 'saldo', 'inativo'