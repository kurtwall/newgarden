# Generated by Django 5.0.1 on 2024-03-02 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0021_delete_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Calendar Events',
                'verbose_name_plural': 'Calendar Events',
            },
        ),
    ]