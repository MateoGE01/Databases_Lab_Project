from rest_framework import viewsets
from .models import Database
from .serializers import DatabaseSerializer, DatabaseGradevsDaysSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Avg, Q, CharField, Value
from django.db.models.functions import Concat
from datetime import datetime

class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

   
    #1 se agrupe por el course_id y se muestre el número de registered y el número de certified
    @action(detail=False, methods=['get'])
    def CourseidRegisteredCertified(self, request):    
        consulta = Database.objects.values('course_id').annotate(registered=Count('id', filter=Q(registered=1)), certified=Count('id', filter=Q(certified=1)))
        
        return Response(consulta)

    #2 conteo de mujeres y hombres, filtrando por grado de educación
    @action(detail=False, methods=['get'])
    def AcademyLevelFemaleAndMaleCount(self, request):       
        consulta = Database.objects.values('loe_di').annotate(female_count=Count('id', filter=Q(gender='f')), Avg_grade_female = Avg('grade', filter=Q(gender='f')),
                                                              male_count=Count('id', filter=Q(gender='m')), Avg_grade_male = Avg('grade', filter=Q(gender='m')))
        return Response(consulta)

    #3y4 eje x: paises, eje y: el porcentaje de registered, viewed, explored certified (ESTO SERA EL FILTRO)
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
    
    #5 pais vs promedio de nota POR PAIS ORDENADO DE MAYOR A MENOR, se exluyeron las notas que tenían 0, porque vuelven los números extremeadamente bajos
    @action(detail=False, methods=['get'])
    def avggradePerCountry(self, request):
        promedio = Database.objects.exclude(grade=0).values('final_cc_cname_di').annotate(avg_grade=Avg('grade')).order_by('-avg_grade')
        
        return Response(list(promedio))
   
    #6 por cada año,mes, dime por pais cuantos empezaron en esa fecha
    @action(detail=False, methods=['get'])
    def StudentsJoinedYearAndMonthEachCountry(self, request):
        year_month = Concat('start_time_di__year', Value('-'), 'start_time_di__month', output_field=CharField())
        students = Database.objects.filter(registered=1).annotate(year_month=year_month).values('year_month', 'final_cc_cname_di').annotate(registrados=Count('id')).order_by('year_month')
        
        return Response(list(students))
    
    