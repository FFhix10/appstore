# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 10:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160628_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='recommendations',
        ),
    ]
