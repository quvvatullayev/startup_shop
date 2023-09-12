from rest_framework import generics
from ..models import StartupModel
from ..serialization import StartupSerializer
from rest_framework import viewsets

class StartupListCreateViews(generics.ListCreateAPIView):
    queryset = StartupModel.objects.all()
    serializer_class = StartupSerializer