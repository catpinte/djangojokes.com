from rest_framework import serializers
from jokes.models import Joke, Tag, Category

class JokeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Joke
        fields = ('question', 'answer', 'created', 'updated','slug')
