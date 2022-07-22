from rest_framework import routers
from event.api import EventViewSet, PlaceViewSet,CategoryViewSet

router = routers.DefaultRouter()
router.register('api/event', EventViewSet, 'event')
router.register('api/place', PlaceViewSet, 'place')
router.register('api/category', CategoryViewSet, 'category')
urlpatterns = router.urls
