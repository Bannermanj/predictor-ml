# Generated by Django 2.0.5 on 2018-05-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor_ap', '0013_auto_20180508_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldcupmatch',
            name='match_date',
            field=models.DateField(max_length=12),
        ),
    ]
