# Generated by Django 2.1.4 on 2019-04-15 07:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0002_auto_20190415_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='matriculas.Estado', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='freserva',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha Reserva'),
        ),
    ]