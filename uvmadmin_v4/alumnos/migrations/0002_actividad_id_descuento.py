# Generated by Django 2.1.4 on 2019-04-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='id_descuento',
            field=models.IntegerField(default=0, verbose_name='Descuento'),
        ),
    ]
