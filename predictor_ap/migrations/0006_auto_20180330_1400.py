# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor_ap', '0005_bundesligateam'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team',
            new_name='PremierLeagueTeam',
        ),
    ]
