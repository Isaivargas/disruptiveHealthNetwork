"""HackProyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin

# urlpatterns = [
    
#     path('admin/', admin.site.urls),
#     path('doc-service/', include('doc-service.urls'))
# ]

# Create your views here.
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from prueba.views import UserViewSet, PreguntaViewSet, RespuestaViewSet, ArticuloViewSet, DoctorViewSet,SintomaViewSet,MedicamentoViewSet,TratamientoViewSet,ArticuloSistemaViewSet,TratamientoMedicamentoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pregunta', PreguntaViewSet)
router.register(r'respuesta',RespuestaViewSet)
router.register(r'Doctor', DoctorViewSet)
router.register(r'Articulo',ArticuloViewSet)
router.register(r'Sintoma',SintomaViewSet)
router.register(r'Medicamento',MedicamentoViewSet)
router.register(r'Tratamiento',TratamientoViewSet)
router.register(r'ArticuloSistema',ArticuloSistemaViewSet)
router.register(r'TratamientoMedicamento',TratamientoMedicamentoViewSet)

#    
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]