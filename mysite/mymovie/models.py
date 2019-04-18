from django.db import models

class Movies(models.Model):
    index = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    images = models.CharField(max_length=255)

class Weathers(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)
    temp = models.CharField(max_length=255)
    wind = models.CharField(max_length=255)
    strength = models.CharField(max_length=255)