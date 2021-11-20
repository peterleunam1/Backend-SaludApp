"""saludapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework import routers
from agendamiento.views import *
from resultados.views import *

router = routers.DefaultRouter()
router.register('usuarios-auth', UsuarioAuthViewSet)
router.register('usuarios', UsuarioViewSet)
router.register('eps', EpsViewSet)
router.register('especialidades', EspecialidadViewSet)
router.register('medicos', MedicoViewSet)
router.register('departamentos', DepartamentoViewSet)
router.register('municipios', MunicipioViewSet)
router.register('citas-medicas', CitasMedicasViewSet)
router.register('examenes-medicos', ExamenMedicoViewSet)
router.register('laboratorio', LaboratorioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
