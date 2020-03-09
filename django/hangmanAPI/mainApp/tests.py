from django.test import TestCase
from mainApp.models import Word

class WordTestCase(TestCase):
    def test_get_random_word(self):
        randomWord = Word
        randomWord = Word.get_random_word(randomWord)
        self.assertTrue(randomWord, type(randomWord) == str)

