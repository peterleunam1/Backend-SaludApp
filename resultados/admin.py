from django.contrib import admin
from resultados.models import *

# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display =  ('muestra','usuario','examen','especialidad','fecha')

admin.site.register(ExamenMedico)
admin.site.register(Laboratorio, LaboratorioAdmin)