from django.db import models


class Person(models.Model):
    govt_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
