# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-26 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0067_uservoterecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='uservoterecord',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
