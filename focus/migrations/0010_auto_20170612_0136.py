# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0009_auto_20170607_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]