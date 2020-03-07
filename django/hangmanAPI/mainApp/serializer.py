from rest_framework import serializers
from .models import getNewWord

class WordSerializer(serializers.ModeSerializer):
    class Meta:
        model = getNewWord
