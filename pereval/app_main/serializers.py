from rest_framework import serializers

from .models import Pereval


class PerevalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = [
            'user',
            'coords',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'level_spring',
            'level_summer',
            'level_autumn',
            'level_winter'
        ]


class PerevalRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'


class PerevalRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        exclude = ['user']


class PerevalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'
