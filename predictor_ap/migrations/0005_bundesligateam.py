# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor_ap', '0004_laligateam'),
    ]

    operations = [
        migrations.CreateModel(
            name='BundesligaTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('league', models.CharField(max_length=100)),
            ],
        ),
    ]
