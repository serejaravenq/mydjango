# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-06 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoinfo',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
