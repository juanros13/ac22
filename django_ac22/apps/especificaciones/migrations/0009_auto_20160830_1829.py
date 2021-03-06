# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 23:29
from __future__ import unicode_literals

import apps.ac22.validators
import apps.especificaciones.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('especificaciones', '0008_auto_20160830_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especificaciones',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to=apps.especificaciones.models.PathAndRename(b'especificaciones'), validators=[apps.ac22.validators.validate_file_extension_pdf_and_zip]),
        ),
        migrations.AlterField(
            model_name='especificaciones',
            name='nombre_anexo',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
    ]
