# Generated by Django 4.1.1 on 2022-10-03 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("note_api", "0003_note_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="note",
            name="owner",
        ),
    ]