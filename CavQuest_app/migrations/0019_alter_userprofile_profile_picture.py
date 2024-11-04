# Generated by Django 4.2.5 on 2023-11-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CavQuest_app", "0018_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(
                default="images/default-avatar.png", upload_to="profile_pictures/"
            ),
        ),
    ]
