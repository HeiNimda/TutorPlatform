# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-18 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.CharField(max_length=64, unique=True, verbose_name='微信ID')),
                ('nickname', models.CharField(blank=True, max_length=64, null=True, verbose_name='微信名称')),
                ('avatar_url', models.URLField(blank=True, help_text='头像', null=True, verbose_name='头像')),
                ('customer_type', models.IntegerField(choices=[(0, '没有注册'), (1, '教师'), (2, '学生')], default=0, help_text='0: 没有注册 1: 教师 2: 学生', verbose_name='用户角色')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
