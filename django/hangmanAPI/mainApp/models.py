from django.db import models
import requests
import hangmanAPI.settings as settings


class Word(models.Model):
    solution = models.CharField(max_length=10)

    def get_random_word(self):
        url = "https://wordsapiv1.p.rapidapi.com/words/"
        querystring = {"random": "true", "lettersMin": 3, "lettersMax": 10}
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': settings.SECRET_KEY
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        entireResponse = response.json()
        return entireResponse['word']
