# Generated by Django 4.2.4 on 2023-08-21 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTask2', '0002_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='Desc',
            new_name='Desc1',
        ),
    ]