# Generated by Django 4.1.7 on 2023-03-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cousin", "0006_alter_cousin_father"),
        ("parent", "0008_alter_parent_daughter_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="parent",
            name="daughter_name",
        ),
        migrations.AddField(
            model_name="parent",
            name="daughter_name",
            field=models.ManyToManyField(related_name="daugther", to="cousin.cousin"),
        ),
    ]