# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 19:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20170201_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_closed',
        ),
    ]
