# Generated by Django 4.2 on 2023-04-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="text",
            field=models.TextField(default=""),
        ),
    ]
