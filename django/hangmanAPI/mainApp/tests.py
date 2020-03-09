from django.test import TestCase
import mainApp.models as mds


class WordTestCase(TestCase):
    def test_get_random_word(self):
        wordPair = mds.Word()
        wordPair.get_random_word()

        # Check the displayWord attribute
        self.assertTrue(type(wordPair.displayWord), str)
        self.assertIs(wordPair.displayWord, '_'*10)

        # Check the private _solution attribute
        self.assertTrue(type(wordPair._solution), str)
        self.assertTrue(wordPair._solution.isalpha(), True)

