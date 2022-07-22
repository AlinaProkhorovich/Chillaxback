from rest_framework import serializers

from event.models import Events, Place, Category


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
