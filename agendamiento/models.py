from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Eps(models.Model):
    id_eps = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = _("Eps")  

class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = _("Especialidades")

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = _("Departamentos")

class Usuario(models.Model):
    identificacion = models.BigIntegerField(primary_key=True) 
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    email = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=30)
    eps = models.ForeignKey(Eps, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str({self.nombres, self.apellidoPaterno})
    class Meta:
        verbose_name_plural = _("Usuarios")

class Medico(models.Model):
    identificacion = models.BigIntegerField(primary_key=True)
    apellido = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    eps = models.ForeignKey(Eps, null=False, blank=False, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str({self.nombres, self.apellido})
    class Meta:
        verbose_name_plural = _("Medicos")

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = _("Municipios")

class CitasMedicas(models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, null=False, blank=False, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return str({self.usuario, self.especialidad, self.fecha})
    class Meta:
        verbose_name_plural = _("Citas medicas")
