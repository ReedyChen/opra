# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-31 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0123_auto_20180731_0853'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SignUpRequests',
            new_name='SignUpRequest',
        ),
    ]