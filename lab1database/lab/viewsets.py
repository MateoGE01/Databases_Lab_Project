from rest_framework import viewsets, mixins
from .models import Database
from .serializers import DatabaseSerializer, DatabaseGradevsDaysSerializer, NotaIndividualSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Avg
from datetime import datetime

class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

    #eje x: paises, eje y: el porcentaje de registered, viewed, explored certified (ESTO SERA EL FILTRO)
    #(NOTA: EL EJE X TIENE QUE ESTAR ORGANIZADO DE MENOR A MAYOR PORCENTAJE)
    @action(detail=False, methods=['get'])
    def CountriesPercentage(self, request):
        field = request.query_params.get('field', None)
        if field not in ['registered', 'viewed', 'explored', 'certified']:
            return Response({'error': 'Debe escribir el campo por el que se filtrará'}, status=400)
        
        total_rows = Database.objects.count()
        field_counts = Database.objects.filter(**{f'{field}': 1}).values('final_cc_cname_di').annotate(Count=Count('id'))
        
        results = []
        
        for item in field_counts:
            results.append({'final_cc_cname_di': item['final_cc_cname_di'], "Percentage": (item['Count'] / total_rows)*100})

        results_sorted = sorted(results, key=lambda x: x['Percentage'])

        
        return Response(results_sorted)
    
    #pais vs promedio de nota POR PAIS ORDENADO DE MAYOR A MENOR, se exluyeron las notas que tenían 0, porque vuelven los números extremeadamente bajos
    @action(detail=False, methods=['get'])
    def avggradePerCountry(self, request):
        promedio = Database.objects.exclude(grade=0).values('final_cc_cname_di').annotate(avg_grade=Avg('grade')).order_by('-avg_grade')
        return Response(list(promedio))


#nota promedio del alumno vs cuantos dias duro activo en el curso. Filtro:Edad
#Tener en cuenta que yob es el año de nacimiento, por lo que para obtener la edad se debe restar el año actual menos yob.
class DatabaseGradevsDaysViewSet(viewsets.GenericViewSet,                   
                      mixins.RetrieveModelMixin,                     
                      mixins.ListModelMixin,): 
    
    serializer_class = DatabaseGradevsDaysSerializer

    def get_queryset(self):
        queryset = Database.objects.all()
        age = self.request.query_params.get('años', None)
        if age is not None:
            age = int(age)
            current_year = datetime.now().year
            queryset = queryset.filter(yob=current_year-age)
        return queryset
    

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
           