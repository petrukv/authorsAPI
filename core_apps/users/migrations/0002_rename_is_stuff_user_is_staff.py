# Generated by Django 5.0.2 on 2024-03-19 21:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_stuff",
            new_name="is_staff",
        ),
    ]
