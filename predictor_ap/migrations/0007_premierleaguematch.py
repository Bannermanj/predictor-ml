# Generated by Django 2.0.5 on 2018-05-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor_ap', '0006_auto_20180330_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremierLeagueMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=12)),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('home_score', models.PositiveSmallIntegerField(default=0)),
                ('away_score', models.PositiveSmallIntegerField(default=0)),
                ('result', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
