# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 22:35
from __future__ import unicode_literals

import apps.ac22.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('especificaciones', '0005_especificaciones_nombre_anexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalEspecificaciones',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombre_documento', models.CharField(max_length=450)),
                ('contenido', models.CharField(max_length=450)),
                ('nombre_anexo', models.CharField(max_length=450)),
                ('anexo', models.TextField(max_length=100, validators=[apps.ac22.validators.validate_file_extension_pdf])),
                ('fecha_creacion', models.DateTimeField(editable=False)),
                ('fecha_modificacion', models.DateTimeField(editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='especificaciones.HistoricalEspecificaciones')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical especificaciones',
            },
        ),
    ]