# Generated by Django 2.1.7 on 2019-05-09 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mymovie', '0010_articlepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepost',
            name='author',
        ),
        migrations.DeleteModel(
            name='ArticlePost',
        ),
    ]
