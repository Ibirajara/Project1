from django.db import models
import datetime

class Mesa(models.Model):
    numero = models.IntegerField( verbose_name='Número', unique=True, help_text='Número da plaqueta da mesa.' )
    TIPOS = (
        ('min', 'Mineira normal'),
        ('mip', 'Mineira pequena'),
        ('tot', 'Totó'),
        ('mig', 'Mineira grande'),
        ('cbc', 'Cumbuca'),
        ('cmp', 'Campineira')
    )
    tipo_mesa = models.CharField(max_length=3, choices=TIPOS, default='min', blank=True, help_text='Escolha o tipo de mesa')
    num_registro = models.IntegerField(default=0, help_text='O número do registro')
    data_cadastro = models.DateField(default=datetime.date.today )
    locada = models.BooleanField(verbose_name='Locada', default=False, editable=False, help_text='Informa se a mesa está locada')

    def __str__(self):
        return self.numero + " - " + self.tipo_mesa


