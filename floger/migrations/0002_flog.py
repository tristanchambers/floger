# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('floger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ingredient_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floger.Ingredient_amount')),
            ],
        ),
    ]
