# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-28 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formchoice',
            name='slug',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
