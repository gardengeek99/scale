# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-08 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0026_auto_20180723_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='source_collection',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='source_sensor',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='source_sensor_class',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='source_task',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='source_ended',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='source_started',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]