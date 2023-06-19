# Generated by Django 4.1.7 on 2023-03-22 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cousin", "0007_alter_cousin_grandfather_alter_cousin_grandmother_and_more"),
        ("grandparent", "0005_grandparent_daughter_name"),
        ("parent", "0009_remove_parent_daughter_name_parent_daughter_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parent",
            name="daughter_name",
            field=models.ManyToManyField(
                blank=True, related_name="daugther", to="cousin.cousin"
            ),
        ),
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
        migrations.AlterField(
            model_name="parent",
            name="mother_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mother_name",
                to="grandparent.grandparent",
            ),
        ),
    ]
