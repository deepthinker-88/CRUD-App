# Generated by Django 4.1.7 on 2023-03-01 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("parent", "0001_initial"),
        ("cousin", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cousin",
            name="parent",
        ),
        migrations.AddField(
            model_name="cousin",
            name="father",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mother",
                to="parent.parent",
            ),
        ),
        migrations.AddField(
            model_name="cousin",
            name="mother",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="father",
                to="parent.parent",
            ),
        ),
    ]