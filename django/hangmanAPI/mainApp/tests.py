from django.test import TestCase
import mainApp.models as mds


class WordTestCase(TestCase):
    def test_get_random_word(self):
        randomWord = mds.Word()
        randomWord.get_random_word()
        self.assertTrue(type(randomWord.solution), str)
        self.assertTrue(randomWord.solution.isalpha(), True)
