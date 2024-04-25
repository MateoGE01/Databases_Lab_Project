from rest_framework import routers
from .viewsets import DatabaseViewSet

app_name = 'lab'

router = routers.DefaultRouter()
router.register('base_de_datos', DatabaseViewSet)