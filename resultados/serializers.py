from django.db.models.fields import Field
from rest_framework import fields, serializers 
from resultados.models import *

class ExamenMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamenMedico
        fields = ('codigo','nombre')

class LaboratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorio
        fields = ('muestra','usuario','fecha','valoracion','examen','especialidad')



