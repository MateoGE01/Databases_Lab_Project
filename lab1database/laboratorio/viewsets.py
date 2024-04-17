from rest_framework import viewsets
from .models import Database
from .serializers import DatabaseSerializer

class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer