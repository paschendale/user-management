from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
