# Generated by Django 4.1.7 on 2023-03-13 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cousin", "0006_alter_cousin_father"),
        ("parent", "0007_remove_parent_son_name_parent_son_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parent",
            name="daughter_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="daughter_name",
                to="cousin.cousin",
            ),
        ),
    ]
