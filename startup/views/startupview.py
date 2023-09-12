from rest_framework import generics
from ..models import StartupModel
from ..serialization import StartupSerializer
from rest_framework import viewsets

class StartupViews(generics.ListCreateAPIView):
    queryset = StartupModel.objects.all()
    serializer_class = StartupSerializer

class StartupView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StartupModel.objects.all()
    serializer_class = StartupSerializer 