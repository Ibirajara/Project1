from django.shortcuts import render
from django.urls import reverse_lazy
from cargo.models import Cargo
from .models import Funcionario
from funcionario.forms import FuncForm
from django.views.generic import ( ListView, UpdateView, CreateView )
from django.contrib.auth.mixins import LoginRequiredMixin

class ListarFuncionarioView(LoginRequiredMixin, ListView):
    login_url='login'
    model = Funcionario
    template_name = 'listarfuncionarios.html'

#Alterar funcionário ** Não existe a possibilidade de se excluir um funcionário. O ideal é torná-lo inativo
class AlterarFuncionarioView(LoginRequiredMixin, UpdateView):

    '''
    ##TODO - Implementar a exibição da empresa na hora que chamar o médoto para alterar
    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super().get_context_data(**kwargs)
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)
'''

    login_url='login'
    model = Funcionario
    template_name = 'alterarFuncionario.html'
    form_class = FuncForm
    success_url=reverse_lazy('listarFuncionarios')



class IncluirFuncionarioView(LoginRequiredMixin, CreateView):
    print(request.session['empresa'])
    login_url='login'
    model = Funcionario
    template_name = 'salvarfuncionario2.html'
    form_class = FuncForm
    success_url = reverse_lazy('listarFuncionarios')
    


