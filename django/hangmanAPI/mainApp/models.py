from django.db import models


class Word(models.Model):
    solution = models.CharField(max_length=10)
