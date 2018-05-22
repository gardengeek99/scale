# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-17 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_scheduler_resource_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler',
            name='resource_level',
            field=models.CharField(choices=[('TOO HIGH', 'TOO HIGH'), ('TOO LOW', 'TOO LOW'), ('GOOD', 'GOOD')], default='GOOD', max_length=10),
        ),
    ]
