from event.models import Events, Place, Category
from rest_framework import viewsets, permissions
from event.serializers import EventSerializer, PlaceSerializer, CategorySerializer
# from django_filters.rest_framework import DjangoFilterBackend


class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['speciality']


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.AllowAny]
    serializer_class = PlaceSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

