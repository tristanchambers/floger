# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floger', '0002_flog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flog',
            name='ingredient_amount',
        ),
    ]