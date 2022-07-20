from django.shortcuts import render


from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, permissions

from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from .renderers import UserJSONRenderer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = User.objects

    @action(methods=["GET"], detail=False)
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    serializer_class = LoginSerializer

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # def home(request):
    #     return render(request, "homepage.html")