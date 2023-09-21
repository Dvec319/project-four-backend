from rest_framework import serializers
from .models import Athlete

class AthleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model to serialize
        model = Athlete
        # fields to show in json
        fields = ('id', 'age', 'name', 'position', 'sport', 'team', 'year')
