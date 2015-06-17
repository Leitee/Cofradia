# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.IntegerField()),
                ('tipo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCategoria', models.CharField(max_length=50)),
                ('descripcionCategoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePublicacion', models.CharField(max_length=100)),
                ('fechaPublicacion', models.DateField()),
                ('fechaCierre', models.DateField()),
                ('descripcion', models.CharField(max_length=300)),
                ('categoria', models.ForeignKey(to='aplicacion.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('user', models.CharField(max_length=20, unique=True)),
                ('pas', models.CharField(max_length=15)),
                ('fNacimiento', models.DateField()),
                ('sexo', models.BooleanField()),
                ('email', models.EmailField(max_length=75)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
        migrations.AddField(
            model_name='postulante',
            name='publicacion',
            field=models.ForeignKey(to='aplicacion.Publicacion'),
        ),
        migrations.AddField(
            model_name='postulante',
            name='usuario',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='publicacion',
            field=models.ForeignKey(to='aplicacion.Publicacion'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='usuario',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
    ]
