# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
