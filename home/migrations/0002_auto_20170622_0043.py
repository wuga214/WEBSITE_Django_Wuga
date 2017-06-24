# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 00:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsup',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='whatsup',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='whatsup',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 6, 22, 0, 43, 36, 642655)),
        ),
    ]
