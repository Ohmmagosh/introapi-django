# Generated by Django 4.1.7 on 2023-02-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("intra_id", models.CharField(max_length=50)),
                ("favorite_language", models.CharField(max_length=50)),
                ("favorite_food", models.CharField(max_length=50)),
                ("favorite_color", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
