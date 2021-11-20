from django.shortcuts import render

from resultados.models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.

class ExamenMedicoViewSet(viewsets.ModelViewSet):
    queryset = ExamenMedico.objects.all()
    serializer_class = ExamenMedicoSerializer

class LaboratorioViewSet(viewsets.ModelViewSet):
    queryset = Laboratorio.objects.all()
    serializer_class = LaboratorioSerializer


