# Generated by Django 2.1.4 on 2019-04-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0003_descuento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='descuento',
        ),
        migrations.AddField(
            model_name='materia',
            name='aplica_dto',
            field=models.BooleanField(default=False, verbose_name='Aplica Descuento'),
        ),
    ]
