# Generated by Django 2.0.5 on 2018-05-07 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor_ap', '0007_premierleaguematch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premierleaguematch',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
