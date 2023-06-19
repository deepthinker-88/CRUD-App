# Generated by Django 4.1.7 on 2023-03-05 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("grandparent", "0004_grandparent_age_grandparent_first_name_and_more"),
        ("parent", "0004_parent_daughter_name_parent_son_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parent",
            name="father_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="father_name",
                to="grandparent.grandparent",
            ),
        ),
    ]