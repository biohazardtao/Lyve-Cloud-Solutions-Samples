# Generated by Django 4.0.4 on 2022-05-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0007_migration_created_at_migration_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='migration',
            name='dest_prefix',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='migration',
            name='filter_date_after',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='migration',
            name='filter_date_before',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='migration',
            name='filter_size_gte',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='migration',
            name='filter_size_lte',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='migration',
            name='src_prefix',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]