from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.ListarMesasView.as_view(), name='listarMesas'),
    path('novo/', views.SalvarMesaView.as_view(), name='incluirMesa' ),
    path('alterar/<int:pk>', views.AlterarMesaView.as_view(), name='alterarMesa'),
]