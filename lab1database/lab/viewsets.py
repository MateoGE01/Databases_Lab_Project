from rest_framework import viewsets, mixins
from .models import Database
from .serializers import DatabaseSerializer, NotaIndividualSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count


class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'


#nota promedio del alumno vs cuantos dias duro activo en e curso. Filtro:Edad
#Este lo tengo que arreglar y hacerlo mejor
class DatabaseGradevsDaysViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin):
    queryset = Database.objects.filter(yob=2000)
    serializer_class = DatabaseSerializer

#nota individual y filtrar por dos cosas: nivel académico y género.
class DatabaseNotaIndividualViewSet(viewsets.GenericViewSet,                   
                      mixins.RetrieveModelMixin,                     
                      mixins.ListModelMixin,):
    serializer_class = NotaIndividualSerializer

    def get_queryset(self):
        queryset = Database.objects.all()
        gender = self.request.query_params.get('gender', None)
        loe_di = self.request.query_params.get('loe_di', None)
        if gender is not None:
            queryset = queryset.filter(gender=gender)
        if loe_di is not None:
            queryset = queryset.filter(loe_di=loe_di)
        return queryset     
    
#
class DatabaseCountriesFilters(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin):
    serializer_class = DatabaseSerializer    
    queryset = Database.objects.all()

    @action(detail=False, methods=['get'])
    def percentage(self, request):
        field = request.query_params.get('field', None)
        if field not in ['registered', 'viewed', 'explored', 'certified']:
            return Response({'error': 'Invalid field'}, status=400)
        
        total_rows = Database.objects.count()
        field_counts = Database.objects.filter(**{f'{field}': 1}).values('final_cc_cname_di').annotate(Count=Count('id'))
        
        results = {}

        for item in field_counts:
            results[item['final_cc_cname_di']] = (item['Count'] / total_rows)*100

        sorted_data = dict(sorted(results.items(), key=lambda item: item[1]))
        
        return Response(sorted_data)
        