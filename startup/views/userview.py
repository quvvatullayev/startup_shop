from rest_framework import generics
from ..models import UserModel
from ..serialization import UserSerializer

class StartupUsers(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class StartupUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
