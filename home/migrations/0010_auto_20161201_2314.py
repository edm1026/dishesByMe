# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-02 05:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
