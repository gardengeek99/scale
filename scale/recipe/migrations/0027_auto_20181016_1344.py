# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-16 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0027_auto_20181008_1756'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recipetype',
            unique_together=set([]),
        ),
    ]
