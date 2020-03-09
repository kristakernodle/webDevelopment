from django.db import models
import requests
import hangmanAPI.settings as settings


class Game(models.Model):
    state = models.BooleanField(default=False)


class Word(models.Model):
    _solution: str = models.CharField(max_length=10)
    displayWord = models.CharField(max_length=10, default='_'*10)

    def get_random_word(self):
        url = "https://wordsapiv1.p.rapidapi.com/words/"
        querystring = {"random": "true", "lettersMin": 10, "lettersMax": 10}
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': settings.SECRET_KEY
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        entireResponse = response.json()
        randomWord = entireResponse['word']
        while not randomWord.isalpha():
            response = requests.request("GET", url, headers=headers, params=querystring)
            entireResponse = response.json()
            randomWord = entireResponse['word']
        self._solution = randomWord
