# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160623_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='top_news',
            field=models.CharField(choices=[('top', 'Top News'), ('not', 'Not')], default='not', max_length=256),
        ),
    ]