# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0012_auto_20171204_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='link',
            field=models.CharField(blank=True, default=None, max_length=280, null=True),
        ),
    ]
