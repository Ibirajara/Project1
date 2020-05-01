
from django.urls import path
from . import views
urlpatterns = [
    path( 'listar/', views.ListarCargosViews.as_view() , name='listarCargos' ),
    path('incluir/', views.CriarCargoView.as_view(), name='criarCargo' ),
    path('alterar/<int:pk>', views.AlterarCargoViews.as_view() , name='alterarCargo'),
    path('excluir/<int:pk>', views.ExcluirCargoView.as_view(), name='excluirCargo'),

]
