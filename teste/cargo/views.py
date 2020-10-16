from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from .models import Cargo
from .forms import CargoForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView, View, RedirectView )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_protect


class ListarCargosViews(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Cargo
    template_name = 'listarcargos.html'

class CriarCargoView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Cargo
    template_name = 'novocargo.html'
    form_class = CargoForm 
    success_url = reverse_lazy('listarCargos')

class AlterarCargoViews(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Cargo
    template_name='novocargo.html'
    form_class = CargoForm
    success_url = reverse_lazy('listarCargos')

class ExcluirCargoView(LoginRequiredMixin, DeleteView):
    login_url='login'
    model = Cargo
    template_name = 'deleteconfirm.html'
    success_url = reverse_lazy('listarCargos')
    



