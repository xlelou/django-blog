# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0003_article_keep_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='keep_num',
            field=models.PositiveIntegerField(default=0, verbose_name=b'\xe6\x94\xb6\xe8\x97\x8f\xe6\x95\xb0'),
        ),
    ]