# Generated by Django 4.1.7 on 2023-04-19 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("grandparent", "0012_alter_grandparent_options"),
        ("cousin", "0008_alter_cousin_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cousin",
            name="grandfather",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="grandfathers",
                to="grandparent.grandparent",
            ),
        ),
        migrations.AlterField(
            model_name="cousin",
            name="grandmother",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="grandmothers",
                to="grandparent.grandparent",
            ),
        ),
    ]