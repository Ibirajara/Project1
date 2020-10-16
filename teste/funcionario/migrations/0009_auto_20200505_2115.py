# Generated by Django 3.0.5 on 2020-05-06 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('funcionario', '0008_auto_20200504_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa', verbose_name='Empresa'),
            preserve_default=False,
        ),
    ]