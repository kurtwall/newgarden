# Generated by Django 5.0.1 on 2024-03-03 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0027_alter_task_options_rename_task_task_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='end_recur',
            new_name='end',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='start_recur',
            new_name='start',
        ),
        migrations.RemoveField(
            model_name='events',
            name='group_id',
        ),
    ]
