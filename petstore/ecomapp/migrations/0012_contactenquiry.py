# Generated by Django 5.0 on 2024-01-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecomapp", "0011_product_age_alter_product_cat"),
    ]

    operations = [
        migrations.CreateModel(
            name="contactenquiry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=60)),
                ("message", models.TextField()),
            ],
        ),
    ]
