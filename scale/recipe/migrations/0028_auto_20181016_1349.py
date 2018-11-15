# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-16 13:49
from __future__ import unicode_literals

from django.db import connection, migrations


def populate_recipe_file(apps, schema_editor):
    RecipeType = apps.get_model('recipe', 'RecipeType')

    qry = 'SELECT name, count(*) FROM recipe_type GROUP BY name'
    with connection.cursor() as cursor:
        cursor.execute(qry)
        for row in cursor.fetchall():
            name = row[0]
            count = row[1]
            if count > 1:
                print '\nUpdating recipe type \'%s\' with %i versions' % (name, count)
                for recipe_type in RecipeType.objects.filter(name=name):
                    new_name = '%s_%s' % (recipe_type.name, recipe_type.version.replace('-', '.'))
                    RecipeType.objects.filter(name=recipe_type.name, version=recipe_type.version).update(name=new_name)


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0027_auto_20181016_1344'),
    ]

    operations = [
        migrations.RunPython(populate_recipe_file),
    ]
