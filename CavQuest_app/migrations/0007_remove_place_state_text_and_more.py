# Generated by Django 4.2.7 on 2023-11-03 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CavQuest_app", "0006_usersubmission_difficulties_difficulty"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="place",
            name="state_text",
        ),
        migrations.RemoveField(
            model_name="usersubmission",
            name="state_text",
        ),
    ]
