# Generated by Django 4.1.7 on 2023-03-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("grandparent", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grandparent",
            name="first_name",
            field=models.CharField(max_length=30),
        ),
    ]