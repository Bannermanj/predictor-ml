# Generated by Django 2.0.5 on 2018-05-08 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor_ap', '0011_worldcupmatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldcupmatch',
            name='away_team_flag',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='worldcupmatch',
            name='home_team_flag',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]