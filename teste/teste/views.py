from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from empresa.models import Empresa
from usuario.forms import UserExtendForm, UserEmpresaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin

class Inicio(LoginRequiredMixin, TemplateView):
    login_url='login'
    template_name = 'index.html'

@csrf_protect
def login_user(request):
    empresas = Empresa.objects.all()
    return render(request, 'login.html', {'empresas': empresas})
@csrf_protect
def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        empresa = request.POST.get('empresa')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['empresa'] = empresa
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos. Favor tentar novamente.')
            return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')

