# Generated by Django 2.1.7 on 2019-04-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymovie', '0003_auto_20190416_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weathers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('weather', models.CharField(max_length=255)),
                ('temp', models.CharField(max_length=255)),
                ('wind', models.CharField(max_length=255)),
                ('strength', models.CharField(max_length=255)),
            ],
        ),
    ]
