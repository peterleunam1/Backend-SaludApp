from django.db.models.fields import Field
from rest_framework import fields, serializers 
from agendamiento.models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('identificacion', 'apellidoPaterno','apellidoMaterno','nombres','email','contrasenia', 'eps')

class UsuarioAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email', 'contrasenia')        

class EpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eps
        fields = ('id_eps','nombre')

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id_especialidad','nombre')


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('identificacion','apellido','nombres','eps','especialidad')

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id_departamento','nombre')

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ('id_municipio', 'nombre','departamento')

class CitasMedicasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitasMedicas
        fields = ('codigo', 'fecha','usuario','medico','especialidad','municipio')




