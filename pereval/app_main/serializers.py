from rest_framework import serializers

from .models import Pereval


class PerevalSerializer(serializers.ModelSerializer):
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
