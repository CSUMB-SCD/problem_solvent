# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20171126_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/_uploads/'),
        ),
    ]