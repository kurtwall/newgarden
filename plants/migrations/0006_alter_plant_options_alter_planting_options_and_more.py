# Generated by Django 5.0.2 on 2024-02-13 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_rename_harvest_date_planting_harvest_dt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plant',
            options={'ordering': ['name', 'variety']},
        ),
        migrations.AlterModelOptions(
            name='planting',
            options={'ordering': ['bed', 'plant']},
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='entry',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='freq',
            field=models.CharField(choices=[('d', 'daily'), ('w', 'weekly'), ('m', 'monthly'), ('y', 'yearly')], max_length=1, verbose_name='frequency'),
        ),
        migrations.AlterField(
            model_name='task',
            name='note',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.IntegerField(choices=[(0, 'start'), (1, 'plant'), (2, 'weed'), (3, 'water'), (4, 'fertilize'), (5, 'sucker'), (6, 'deadhead'), (7, 'pot up'), (100, 'other')]),
        ),
    ]
