# Generated by Django 5.1.1 on 2024-09-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ais', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='nim',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='nip',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
