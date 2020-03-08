from django.db import models


class getNewWord(models.Model):
     randomWord = models.CharField(max_length=10)
