from django.shortcuts import render
from agendamiento.models import *
from rest_framework import viewsets
from .serializers import *


# Create your views here.
class UsuarioAuthViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioAuthSerializer
    
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EpsViewSet(viewsets.ModelViewSet):
    queryset = Eps.objects.all()
    serializer_class = EpsSerializer

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class CitasMedicasViewSet(viewsets.ModelViewSet):
    queryset = CitasMedicas.objects.all()
    serializer_class = CitasMedicasSerializer





