# Generated by Django 2.1.7 on 2019-04-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymovie', '0006_auto_20190418_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]