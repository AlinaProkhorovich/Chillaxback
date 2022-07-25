from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, permissions

# from django.contrib.auth.models import User
from core.models import Profile, Comment
from core.serializers import RegistrationSerializer, LoginSerializer, UserSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Profile.objects

    permission_classes_by_action = {
        "create": [permissions.AllowAny, ],
    }

    def get_permissions(self):
        if self.action in self.permission_classes_by_action:
            permissions = self.permission_classes_by_action[self.action]
        else:
            permissions = self.permission_classes
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        if self.action == "create":
            return RegistrationSerializer
        return self.serializer_class

    @action(methods=["GET"], detail=False)
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    serializer_class = LoginSerializer

    def get(self, request, format=None):
        users = Profile.objects.all()
        serializer = LoginSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # def home(request):
    #     return render(request, "homepage.html")
class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'token': serializer.data.get('token', None),},status=status.HTTP_201_CREATED,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['speciality']