# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=450)),
                ('abreviatura', models.CharField(max_length=5)),
                ('clave', models.CharField(max_length=5)),
                ('fecha_creacion', models.DateTimeField(editable=False)),
                ('fecha_modificacion', models.DateTimeField(editable=False)),
            ],
        ),
    ]