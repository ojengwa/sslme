# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 00:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160303_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationmodel',
            old_name='postcode',
            new_name='place_id',
        ),
    ]
