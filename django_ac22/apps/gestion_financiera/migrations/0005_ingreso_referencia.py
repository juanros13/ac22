# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_financiera', '0004_ingreso_cuenta'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='referencia',
            field=models.CharField(blank=True, max_length=450, null=True),
        ),
    ]