# Generated by Django 4.2.5 on 2023-11-04 21:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CavQuest_app", "0008_place_latitude_place_longitude_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="place",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]