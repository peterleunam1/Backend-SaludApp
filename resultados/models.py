from django.db import models
from agendamiento.models import *
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class ExamenMedico(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = _("Examenes medicos")

class Laboratorio(models.Model):
    muestra = models.AutoField(primary_key=True)
    fecha = models.DateField()
    valoracion = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    examen= models.ForeignKey(ExamenMedico, null=False, blank=False, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str({self.usuario, self.especialidad, self.fecha})
    class Meta:
        verbose_name_plural = _("Resultados de Laboratorio")