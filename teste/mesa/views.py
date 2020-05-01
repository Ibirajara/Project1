from django.shortcuts import render
from django.views.generic.edit import ( CreateView, UpdateView )
from django.views.generic.list import ListView
from mesa.models import Mesa
from mesa.forms import MesaForm
from django.urls import reverse_lazy

# Create your views here.
class ListarMesasView(ListView):
    model = Mesa
    template_name = 'listarMesas.html'

class SalvarMesaView(CreateView):
    model = Mesa
    template_name = 'salvarmesa.html'
    form_class = MesaForm
    success_url = reverse_lazy('listarMesas')

class AlterarMesaView(UpdateView):
    model = Mesa
    template_name = 'salvarmesa.html'
    form_class = MesaForm
    success_url = reverse_lazy('listarMesas')

