from django.urls import path,include

from rest_framework import routers

from core.views import LoginAPIView, UserViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("comment", CommentViewSet)

app_name = 'authentication'
urlpatterns = [

    path('users/login/', LoginAPIView.as_view()),


] + router.urls



