from django.shortcuts import render
from django.conf import settings
from django.template import loader
from django.http import HttpResponse


from .models import Word
import requests


def dispRandomWord(request):
    url = "https://wordsapiv1.p.rapidapi.com/words/"
    querystring = {"random": "true", "lettersMin": 3, "lettersMax": 10}
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': settings.SECRET_KEY
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    entireResponse = response.json()
    Word._solution = entireResponse['word']

    return render(request, 'dispRandomWord.html', context={'randomWord': Word._solution})
