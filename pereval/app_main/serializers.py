from rest_framework import serializers

from .models import Pereval, User, Coords, Image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'surname', 'name', 'patronym']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image', 'title']


class PerevalCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ['user', 'coords', 'images', 'beauty_title', 'title', 'other_titles', 'connect', 'level_spring',
                  'level_summer', 'level_autumn', 'level_winter']

    def create(self, validated_data):
        user_dict = validated_data.pop('user')
        coords_dict = validated_data.pop('coords')
        images_list = validated_data.pop('images')
        user = User.objects.create(**user_dict)
        coords = Coords.objects.create(**coords_dict)
        pereval = Pereval.objects.create(**validated_data, user=user, coords=coords)
        for img in images_list:
            image = img.pop('image')
            title = img.pop('title')
            Image.objects.create(pereval=pereval, image=image, title=title)
        return pereval


class PerevalRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'


class PerevalRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        exclude = ['id', 'user', 'status']


class PerevalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'
