# Generated by Django 2.2.1 on 2019-10-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0005_auto_20191019_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='step',
            field=models.IntegerField(default=1),
        ),
    ]
