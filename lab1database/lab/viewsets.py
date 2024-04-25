from rest_framework import viewsets
from rest_framework.response import Response
from .models import Database
from .serializers import DatabaseSerializer
from django_filters.rest_framework import DjangoFilterBackend

class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    print(f'No.Filas: {len(queryset)}')
    serializer_class = DatabaseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'
    
    