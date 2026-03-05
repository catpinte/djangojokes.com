from jokes.models import Joke, Category, Tag
from .serializers import JokeSerializer
from .filters import JokeFilter
from rest_framework_api_key.permissions import HasAPIKey

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class JokeListView(ListAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
    permission_classes = [HasAPIKey]
    filter_backends = [DjangoFilterBackend]
    filterset_class = JokeFilter