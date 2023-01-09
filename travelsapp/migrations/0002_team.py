# Generated by Django 4.1.3 on 2022-12-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('dept', models.TextField()),
            ],
        ),
    ]
