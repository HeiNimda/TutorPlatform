# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-24 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_usehelp'),
    ]

    operations = [
        migrations.AddField(
            model_name='reason',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='是否选中'),
        ),
    ]
