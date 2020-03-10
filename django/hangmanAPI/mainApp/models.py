from django.db import models
import requests
import hangmanAPI.settings as settings
import uuid


class MyUUIDClass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)


class Game(models.Model):
    gameID = models.ForeignKey(MyUUIDClass, models.CASCADE, blank=True)
    state = models.BooleanField(default=False)

    def start(self):
        self.state = True


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
