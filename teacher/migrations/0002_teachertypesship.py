# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-10 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20180310_1537'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherTypesShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher', verbose_name='教师')),
                ('teacher_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.TeacherType', verbose_name='教学特点')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]