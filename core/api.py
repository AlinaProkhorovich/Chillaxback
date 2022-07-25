from event.models import Events, Place, Category
from rest_framework import viewsets, permissions
from event.serializers import EventSerializer, PlaceSerializer, CategorySerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]



class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlaceSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer