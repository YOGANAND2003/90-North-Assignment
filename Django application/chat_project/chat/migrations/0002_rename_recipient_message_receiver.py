# Generated by Django 5.1.5 on 2025-01-17 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message",
            old_name="recipient",
            new_name="receiver",
        ),
    ]