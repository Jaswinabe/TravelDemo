# Generated by Django 4.1.3 on 2022-12-06 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='image',
            new_name='img',
        ),
    ]
