# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-27 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0048_auto_20180913_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='source_collection',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='source_sensor',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='source_sensor_class',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='source_task',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='source_ended',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='source_started',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]