# Generated by Django 5.0.7 on 2024-11-15 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coffee", "0002_alter_coffee_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
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
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "coffee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="coffee.coffee"
                    ),
                ),
            ],
        ),
    ]
