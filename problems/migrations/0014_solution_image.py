# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0013_solution_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/_uploads/'),
        ),
    ]
