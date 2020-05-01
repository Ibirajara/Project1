from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from .models import Cargo
from .forms import CargoForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, View, RedirectView )


class ListarCargosViews(ListView):
    model = Cargo
    template_name = 'listarcargos.html'

class CriarCargoView(CreateView):
    model = Cargo
    template_name = 'novocargo.html'
    form_class = CargoForm 
    success_url = reverse_lazy('listarCargos')

class AlterarCargoViews(UpdateView):
    model = Cargo
    template_name='novocargo.html'
    form_class = CargoForm
    success_url = reverse_lazy('listarCargos')

class ExcluirCargoView(DeleteView):
    model = Cargo
    template_name = 'deleteconfirm.html'
    success_url = reverse_lazy('listarCargos')
    



