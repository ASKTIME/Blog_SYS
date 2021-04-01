# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-04-01 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='用户手机号'),
        ),
    ]