# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 16:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obj',
            name='buy_address',
            field=models.TextField(default='no address', max_length=2048, verbose_name='\u8d2d\u4e70\u5730\u70b9'),
        ),
        migrations.AddField(
            model_name='obj',
            name='buy_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 26, 16, 5, 30, 584429), verbose_name='\u8d2d\u4e70\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='obj',
            name='category',
            field=models.CharField(default='no category', max_length=256, verbose_name='\u7c7b\u522b'),
        ),
        migrations.AddField(
            model_name='obj',
            name='type',
            field=models.CharField(default='no type', max_length=256, verbose_name='\u578b\u53f7'),
        ),
    ]
