
from rest_framework import routers
from .viewsets import DatabaseViewSet

app_name = "laboratorio"

router = routers.DefaultRouter()
router.register("database", DatabaseViewSet)