# Generated by Django 2.1.7 on 2019-04-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymovie', '0007_auto_20190418_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
