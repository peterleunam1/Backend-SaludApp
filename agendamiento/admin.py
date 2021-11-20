from django.contrib import admin
from agendamiento.models import *

# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    list_display =  ('identificacion', 'nombres', 'apellidoPaterno', 'eps', 'email')

class CitasMedicasAdmin(admin.ModelAdmin):
    list_display =  ('codigo', 'usuario', 'fecha', 'medico', 'especialidad', 'municipio')

class MedicoAdmin(admin.ModelAdmin):
    list_display =  ('identificacion','nombres','apellido','eps')

class MunicipioAdmin(admin.ModelAdmin):
    list_display =  ('nombre','departamento')

admin.site.register(Eps)
admin.site.register(Especialidad)
admin.site.register(Departamento)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Municipio,MunicipioAdmin)
admin.site.register(CitasMedicas, CitasMedicasAdmin)

