from django.db import models
import hangmanAPI.settings as settings
import requests


class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)


class Word(models.Model):
    solutionWord = models.CharField(max_length=10)

    def getrandomword(self):
        url = "https://wordsapiv1.p.rapidapi.com/words/"
        querystring = {"random": "true", "lettersMin": 3, "lettersMax": 10}
        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': settings.SECRET_KEY
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()
        return response['word']


class Game(models.Model):
    state = models.BooleanField()
    gamesPlayed = models.PositiveSmallIntegerField()
    uniqueID = MyUUIDModel.id

    def start(self):
        self.state = True
        Word.solutionWord = Word.getrandomword()
        self.uniqueID = MyUUIDModel.id

    def stop(self):
        self.state = False


class Guess(models.Model):
    currentLetter = models.CharField(max_length=1)
    prevGuesses = models.CharField(max_length=10)  # Could be the number of guesses before you lose (try/accept)

    def check(self):
        if self.currentLetter in Word.solutionWord:
            return [True, self.prevGuesses]
        self.prevGuesses = self.prevGuesses + self.currentLetter
        return [False, self.prevGuesses]