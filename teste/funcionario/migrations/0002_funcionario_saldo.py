# Generated by Django 3.0.5 on 2020-04-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Saldo'),
        ),
    ]
