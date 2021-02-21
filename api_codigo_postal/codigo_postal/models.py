#https://docs.djangoproject.com/en/3.1/topics/db/models/
# codigo_postal/models.py
from django.db import models


# Clase CodigoPostal, que deriva de la clase Model
class CodigoPostal(models.Model):
    # An id field is added automatically.
    codigo = models.CharField(max_length=5)
    asentamiento = models.CharField(max_length=60)
    tipo_asentamiento = models.CharField(max_length=20)
    municipio = models.CharField(max_length=35)
    estado = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=25)
    zona = models.CharField(max_length=20) 
    def __str__(self):
        return self.codigo