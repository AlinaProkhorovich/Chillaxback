from django.urls import path,include

from rest_framework import routers

from core.views import LoginAPIView, UserViewSet, RegistrationAPIView

router = routers.DefaultRouter()
router.register("users", UserViewSet)

app_name = 'authentication'
urlpatterns = [

    path('users/login/', LoginAPIView.as_view()),
    path('users/signup', RegistrationAPIView.as_view()),


] + router.urls
