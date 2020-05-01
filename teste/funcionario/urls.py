
from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.ListarFuncionarioView.as_view() , name='listarFuncionarios' ),
    path('incluir/', views.IncluirFuncionarioView.as_view(), name='incluirFuncionario'),
    path('alterar/<int:pk>', views.AlterarFuncionarioView.as_view(), name='alterarFuncionario'),
    
]
