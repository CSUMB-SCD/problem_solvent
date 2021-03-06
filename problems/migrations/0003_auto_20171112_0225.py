# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 02:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problem_long_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='problem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Category'),
        ),
    ]
