from rest_framework import viewsets
from .models import Database
from .serializers import DatabaseSerializer, DatabaseGradevsDaysSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Avg, Q
from datetime import datetime

class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DatabaseSerializer

    #1 nota promedio del alumno vs cuantos dias duro activo en el curso. Filtro:Edad
    #Tener en cuenta que yob es el año de nacimiento, por lo que para obtener la edad se debe restar el año actual menos yob.
    @action(detail=False, methods=['get'])
    def Grade_vs_DaysActive(self, request):
        age = request.query_params.get('age', None)
        if age is None:
            return Response({'error': 'Debe escribir la edad por la que se filtrará'}, status=400)
        age = int(age)
        current_year = datetime.now().year 
        datos_edad = Database.objects.filter(yob=current_year-age).exclude(grade__isnull=True)
        serializer = DatabaseGradevsDaysSerializer(datos_edad, many=True)
        return Response(serializer.data)

    #2 conteo de mujeres y hombres, filtrando por grado de educación
    @action(detail=False, methods=['get'])
    def AcademyLevelFemaleAndMaleCount(self, request):
        loe_di = request.query_params.get('loe_di', None)
        if loe_di is None:
            return Response({'error': 'Debe escribir el nivel de educación por el que se filtrará'}, status=400)
        
        consulta = Database.objects.filter(loe_di=loe_di).values('loe_di').annotate(female_count=Count('id', filter=Q(gender='f')), 
                                                                                    male_count=Count('id', filter=Q(gender='m')))
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
   
    #6por fecha de ingreso (start_time_DI	The date when the student started the course. (Date)), cuantos alumos se inscribieron por pais
    #como solo hay dos años que te los agrupe por año y mes
    @action(detail=False, methods=['get'])
    def StudentsJoinedYearAndMonth(self, request):
        year = request.query_params.get('year', None)
        if year is None:
            return Response({'error': 'Debe escribir el año por el que se filtrará'}, status=400)
        month = request.query_params.get('month', None)
        if month is None:
            return Response({'error': 'Debe escribir el mes por el que se filtrará'}, status=400)
        students = Database.objects.filter(start_time_di__year=year, start_time_di__month=month).values('final_cc_cname_di').annotate(Count('id'))
        return Response(list(students))