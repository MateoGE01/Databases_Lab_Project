from django.db import models




class Database(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha_publicacion = models.DateField()
    pais_prision = models.CharField(max_length=100)
    consulado = models.CharField(max_length=100)
    delito = models.CharField(max_length=100)
    extraditado_y_o_repatriado = models.CharField(max_length=100)
    situacion_juridica = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    grupo_edad = models.CharField(max_length=50)
    ubicacion_pais = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    latitud = models.FloatField()
    longitud = models.FloatField()

    class Meta:
        db_table = 'colombianos_detenidos_exterior_tabla'

    def __str__(self):
        return str(self.id)
    
    