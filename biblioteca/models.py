from django.db import models

class autor(models.Model):
    nombre = models.CharField(max_length=100)
    lugar_nacimiento = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField()
    
    def __str__(self):
        return self.nombre

class libro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor= models.ForeignKey(autor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo