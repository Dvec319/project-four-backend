# Generated by Django 4.2.5 on 2023-09-21 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sport', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
