# Generated by Django 4.2.1 on 2023-06-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminatorWeather', '0002_alter_forecast_averagetem_alter_forecast_maxtem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abnormal',
            name='year',
            field=models.IntegerField(),
        ),
    ]
