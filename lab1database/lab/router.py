from rest_framework import routers
from .viewsets import DatabaseViewSet, DatabaseGradevsDaysViewSet, DatabaseNotaIndividualViewSet


app_name = 'lab'

router = routers.DefaultRouter()
router.register('base_de_datos', DatabaseViewSet)
router.register('base_de_datos_grade_vs_days', DatabaseGradevsDaysViewSet, basename='base_de_datos_grade_vs_days')
router.register('base_de_datos_nota_individual', DatabaseNotaIndividualViewSet, basename='base_de_datos_nota_individual')