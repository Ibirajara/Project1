from django.shortcuts import render
from django.urls import reverse_lazy
from cargo.models import Cargo
from .models import Funcionario
from funcionario.forms import FuncForm
from django.views.generic import ( ListView, UpdateView, CreateView )

class ListarFuncionarioView(ListView):
    model = Funcionario
    template_name = 'listarfuncionarios.html'

#Alterar funcionário ** Não existe a possibilidade de se excluir um funcionário. O ideal é torná-lo inativo
class AlterarFuncionarioView(UpdateView):
    model = Funcionario
    template_name = 'salvarFuncionario2.html'
    form_class = FuncForm
    success_url = reverse_lazy('listarFuncionarios')

class IncluirFuncionarioView(CreateView):
    model = Funcionario
    template_name = 'salvarfuncionario2.html'
    form_class = FuncForm
    success_url = reverse_lazy('listarFuncionarios')




