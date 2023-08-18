# Generated by Django 4.2.2 on 2023-07-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_post", "0001_initial"),
        ("core_user", "0002_user_avatar_user_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="post_liked",
            field=models.ManyToManyField(related_name="liked_by", to="core_post.post"),
        ),
    ]
