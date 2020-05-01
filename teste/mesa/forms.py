from django.forms import ModelForm
from mesa.models import Mesa


class MesaForm(ModelForm):
    class Meta:
        model = Mesa
        fields = [ 'numero', 'tipo_mesa',  'num_registro', 'data_cadastro' ]

