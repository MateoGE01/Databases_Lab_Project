from django.db import models

#EL CAMBIO ÚNICO ES AQUÍ PARA DJANGO
#HAY QUE CAMBIAR TODOS LOS ATRIBUTOS POR EL DE LA NUEVA TABLA
class Database(models.Model):
    FECHA_PUBLICACION = models.DateField()
    PAIS_PRISION = models.CharField(max_length=100)
    CONSULADO = models.CharField(max_length=100)
    DELITO = models.CharField(max_length=100)
    EXTRADITADO_Y_O_REPATRIADO = models.CharField(max_length=100)
    SITUACION_JURIDICA = models.CharField(max_length=100)
    GENERO = models.CharField(max_length=50)
    GRUPO_EDAD = models.CharField(max_length=50)
    UBICACION_PAIS = models.CharField(max_length=255)
    CANTIDAD = models.IntegerField()
    LATITUD = models.FloatField()
    LONGITUD = models.FloatField()

    def __str__(self):
        return self.FECHA_PUBLICACION
    
    