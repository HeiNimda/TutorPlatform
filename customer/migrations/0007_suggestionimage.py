# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20180322_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True, verbose_name='图片')),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerSuggestion', verbose_name='投诉表')),
            ],
            options={
                'verbose_name': '投诉图片',
                'verbose_name_plural': '投诉图片',
            },
        ),
    ]
