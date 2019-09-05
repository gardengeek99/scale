# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-25 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0008_occurred_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricserror',
            name='occurred',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='metricsingest',
            name='occurred',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='metricsjobtype',
            name='occurred',
            field=models.DateField(db_index=True),
        ),
    ]