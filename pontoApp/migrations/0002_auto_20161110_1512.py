# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
