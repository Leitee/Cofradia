# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='descripcionCategoria',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='nombreCategoria',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='fechaPublicacion',
            new_name='fechaInicio',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='nombrePublicacion',
            new_name='nombre',
        ),
    ]
