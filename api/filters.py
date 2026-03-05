from django_filters import rest_framework as filters
from jokes.models import Joke

class JokeFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='question', lookup_expr='icontains')        

    class Meta:
        model = Joke
        fields = ['question']
