# Generated by Django 4.2.2 on 2023-06-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_order_coupon_order_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="email"),
        ),
    ]
