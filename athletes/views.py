from rest_framework import viewsets, permissions
from .models import Athlete
from .serializers import AthleteSerializer

# Create your views here.

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.AllowAny]
