# Generated by Django 4.1.7 on 2023-03-01 21:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("grandparent", "0002_alter_grandparent_first_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="grandparent",
            name="age",
        ),
        migrations.RemoveField(
            model_name="grandparent",
            name="first_name",
        ),
    ]
