# Generated by Django 5.0.1 on 2024-02-15 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plants", "0011_alter_bed_options_alter_journalentry_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="freq",
        ),
        migrations.AlterField(
            model_name="journalentry",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="plants.task"
            ),
        ),
    ]
