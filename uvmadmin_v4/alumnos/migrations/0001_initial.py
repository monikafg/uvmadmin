# Generated by Django 2.1.4 on 2019-04-15 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_actividad', models.CharField(max_length=100, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'actividad',
                'verbose_name_plural': 'actividades',
                'ordering': ['des_actividad'],
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=20, unique=True, verbose_name='Documento')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido1', models.CharField(max_length=20, verbose_name='Primer Apellido')),
                ('apellido2', models.CharField(max_length=20, verbose_name='Segundo Apellido')),
                ('des_municipio', models.CharField(default='', max_length=100, verbose_name='Municipio')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('cod_postal', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código Postal')),
                ('telefono1', models.CharField(max_length=20, verbose_name='Teléfono 1')),
                ('telefono2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono 2')),
                ('email1', models.EmailField(max_length=100, verbose_name='Correo Electrónico 1')),
                ('email2', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Correo Electrónico 2')),
                ('nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Genero')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='personas', verbose_name='Foto')),
                ('residente', models.BooleanField(default=False, verbose_name='Residente')),
                ('recibirmail', models.BooleanField(default=False, verbose_name='Recibir Mail')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Actividad', verbose_name='Actividad')),
            ],
            options={
                'verbose_name': 'alumno',
                'verbose_name_plural': 'alumnos',
                'db_table': 'alumnos_alumno',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_municipio', models.SmallIntegerField(verbose_name='Código Municipio')),
                ('des_municipio', models.CharField(max_length=100, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'municipio',
                'verbose_name_plural': 'municipio',
                'ordering': ['des_municipio'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_pais', models.CharField(max_length=2, verbose_name='Código')),
                ('des_pais', models.CharField(max_length=100, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'pais',
                'verbose_name_plural': 'paises',
                'ordering': ['des_pais'],
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_provincia', models.CharField(max_length=100, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'provincia',
                'verbose_name_plural': 'provincias',
                'ordering': ['des_provincia'],
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_documento', models.CharField(max_length=100, verbose_name='Descripción')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'documento',
                'verbose_name_plural': 'documentos',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='municipio',
            name='cod_provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Provincia', verbose_name='Provincia'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='pais',
            field=models.ForeignKey(default=51, on_delete=django.db.models.deletion.CASCADE, to='alumnos.Pais', verbose_name='Pais'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='provincia',
            field=models.ForeignKey(default=35, on_delete=django.db.models.deletion.CASCADE, to='alumnos.Provincia', verbose_name='Provincia'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='tipo_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.TipoDocumento', verbose_name='Tipo Documento'),
        ),
        migrations.AlterUniqueTogether(
            name='municipio',
            unique_together={('cod_provincia', 'cod_municipio')},
        ),
    ]