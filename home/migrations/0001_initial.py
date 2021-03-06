# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeTitle', models.CharField(max_length=150)),
                ('recipeImage', models.CharField(max_length=1000)),
                ('courseType', models.CharField(max_length=30)),
                ('mealType', models.CharField(max_length=30)),
                ('ingredients', models.CharField(max_length=2000)),
                ('directions', models.CharField(max_length=3000)),
            ],
        ),
    ]
