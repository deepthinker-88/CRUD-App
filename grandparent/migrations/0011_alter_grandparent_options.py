# Generated by Django 4.1.7 on 2023-04-07 10:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("grandparent", "0010_grandparent_son_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="grandparent",
            options={"verbose_name_plural": "My Grandparents"},
        ),
    ]
