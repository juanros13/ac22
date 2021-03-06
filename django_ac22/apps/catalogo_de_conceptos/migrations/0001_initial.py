# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 23:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obras', '0006_auto_20160902_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agrupador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=100)),
                ('concepto', models.CharField(max_length=450)),
                ('fecha_creacion', models.DateTimeField(editable=False)),
                ('fecha_modificacion', models.DateTimeField(editable=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.Obra')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogo_de_conceptos.Agrupador')),
                ('usuario_creo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=100)),
                ('concepto', models.CharField(max_length=450)),
                ('unidad', models.CharField(max_length=150)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=12)),
                ('fecha_creacion', models.DateTimeField(editable=False)),
                ('fecha_modificacion', models.DateTimeField(editable=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.Obra')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogo_de_conceptos.Concepto')),
                ('usuario_creo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
