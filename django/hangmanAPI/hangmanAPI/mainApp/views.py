from django.shortcuts import render
import requests
# Create your views here.
from hangmanAPI import settings

url = "https://wordsapiv1.p.rapidapi.com/words/"
querystring = {"random": "true"}
headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': settings.APIKEY_WORDSAPI
}
response = requests.request("GET", url, headers=headers, params=querystring)