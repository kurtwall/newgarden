# Generated by Django 5.0.2 on 2024-02-13 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_rename_num_bed_bed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='bed',
            field=models.IntegerField(unique=True, verbose_name='bed number'),
        ),
    ]