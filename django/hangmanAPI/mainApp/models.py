from django.db import models
import requests


class getNewWord(models.Model):
     randomWord = models.CharField(max_length=10)