# Generated by Django 4.2.5 on 2023-09-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0002_athlete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
