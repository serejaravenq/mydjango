# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-20 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_asdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='myTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
