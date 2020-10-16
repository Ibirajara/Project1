from django.db import models
from django.utils import timezone
from cargo.models import Cargo
from empresa.models import Empresa
from empresa.forms import EmpresaForm
from django.core.exceptions import ValidationError
from teste import settings
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf  = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20, verbose_name='Telefone', blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE,  verbose_name='Cargo' )
    nascimento = models.DateField(verbose_name='Nascimento', blank=True, null=True )
    saldo = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Saldo', default=0)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Empresa' )
    inativo = models.BooleanField(default=False, verbose_name='Inativo')
    data_cadastro = models.DateField(auto_now_add=timezone.now , editable=False, blank=True)

    def __str__(self):
        return self.nome, self.id


