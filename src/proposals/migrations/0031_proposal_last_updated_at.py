# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-22 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0030_auto_20170121_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkproposal',
            name='last_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated at'),
        ),
        migrations.AddField(
            model_name='tutorialproposal',
            name='last_updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='last updated at'),
        ),
    ]
