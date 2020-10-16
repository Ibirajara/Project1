from django.shortcuts import render
from django.views.generic.edit import ( CreateView, UpdateView )
from django.views.generic.list import ListView
from mesa.models import Mesa
from mesa.forms import MesaForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ListarMesasView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Mesa
    template_name = 'listarMesas.html'

class SalvarMesaView(LoginRequiredMixin, CreateView):
    login_url='login'
    model = Mesa
    template_name = 'salvarmesa.html'
    form_class = MesaForm
    success_url = reverse_lazy('listarMesas')

class AlterarMesaView(LoginRequiredMixin, UpdateView):
    login_url='login'
    model = Mesa
    template_name = 'salvarmesa.html'
    form_class = MesaForm
    success_url = reverse_lazy('listarMesas')

