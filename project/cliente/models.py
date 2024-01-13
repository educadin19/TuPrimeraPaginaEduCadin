from django.db import models

class Clase(models.Model):
    nombre = models.CharField(max_length =100)
    duracion = models.CharField(max_length= 3)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

class Profesor(Persona):
    clase_id = models.ForeignKey(Clase, null = True, blank = True, on_delete = models.SET_NULL)
    def __str__(self):
        return self.nombre

class Usuario(Persona):
    clase_id = models.ForeignKey(Clase, null = True, blank = True, on_delete = models.SET_NULL)