# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 06:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20170616_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='jenis_item',
            new_name='katetori_item',
        ),
    ]