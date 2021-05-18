# Generated by Django 3.0.8 on 2020-10-02 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0002_auto_20201002_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aqiprediction',
            old_name='h',
            new_name='Atmospheric_Pressure',
        ),
        migrations.RenameField(
            model_name='aqiprediction',
            old_name='slp',
            new_name='Average_Humidity',
        ),
        migrations.RenameField(
            model_name='aqiprediction',
            old_name='t',
            new_name='Average_Temperature',
        ),
        migrations.RenameField(
            model_name='aqiprediction',
            old_name='tm',
            new_name='Average_Visibility',
        ),
        migrations.RenameField(
            model_name='aqiprediction',
            old_name='tm1',
            new_name='Average_Wind_Speed',
        ),
        migrations.RenameField(
            model_name='aqiprediction',
            old_name='v',
            new_name='Maximum_Temperature',
        ),
        migrations.RenameField(
            model_name='aqiprediction',
            old_name='vm',
            new_name='Maximum_Wind_Speed',
        ),
        migrations.RenameField(
            model_name='aqiprediction',
            old_name='vv',
            new_name='Minimum_Temperature',
        ),
    ]
