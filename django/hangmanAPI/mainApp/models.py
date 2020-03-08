from django.db import models
import uuid


class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class GetNewWord(models.Model):
    randomWord = models.CharField(max_length=10)


class Game(models.Model):
    state = models.BooleanField
    gamesPlayed = models.AutoField
    uniqueID = models.UUIDField

    def start(self):
        solution = GetNewWord.randomWord
        self.uniqueID = MyUUIDModel.id

        # solutions dictionary add uniqueID: solution

class Guess(models.Model):
    currentLetter = models.CharField(max_length=1)
    prevGuesses = models.CharField(max_length=10)  # Could be the number of guesses before you lose (try/accept)

    def check(self):
        if self.currentLetter in solutions[Game.uniqueID]:
            return True
        self.prevGuesses = self.prevGuesses + self.currentLetter
        return False
