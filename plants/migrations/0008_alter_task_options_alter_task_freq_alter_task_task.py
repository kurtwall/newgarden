# Generated by Django 5.0.2 on 2024-02-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0007_alter_task_freq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['task']},
        ),
        migrations.AlterField(
            model_name='task',
            name='freq',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly'), ('Quarterly', 'Quarterly'), ('Other', 'Other')], max_length=20, verbose_name='frequency'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(max_length=20),
        ),
    ]
