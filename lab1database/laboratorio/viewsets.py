from rest_framework import viewsets
from .models import Database
from .serializers import DatabaseSerializer
from django_filters.rest_framework import DjangoFilterBackend


class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    print(f'No.Filas: {len(queryset)}')
    serializer_class = DatabaseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

    """
    1. por genero, cantidad de detenidos vs prisionpais
    2. por año, tenidos vs pais
    3. por año, cantidad de delito vs tipo de delito
    4. por genero, cantidad de delito vs tipo de delito
    5. por año, cantidad de si y cantidadad de no EXTRADITADO Y O REPATRIADO
    """    
