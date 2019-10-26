from django.shortcuts import render

# Create your views here.
import django_filters.rest_framework
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Pregunta, Doctor, Respuesta, Articulo, Sintoma, Medicamento ,Tratamiento, ArticuloSistema,TratamientoMedicamento

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Serializers define the API representation.
class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

# ViewSets define the view behavior.
class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	


# Serializers define the API representation.
class RespuestaSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Respuesta
        fields = '__all__'

# ViewSets define the view behavior.
class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	
#/////////
# Serializers define the API representation.
class DoctorSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Doctor
        fields = '__all__'

# ViewSets define the view behavior.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	

# Serializers define the API representation.
class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Articulo
        fields = '__all__'

# ViewSets define the view behavior.
class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	

# Serializers define the API representation.
class SintomaSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Sintoma
        fields = '__all__'

# ViewSets define the view behavior.
class SintomaViewSet(viewsets.ModelViewSet):
    queryset = Sintoma.objects.all()
    serializer_class = SintomaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	




# Serializers define the API representation.
class MedicamentoSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Medicamento
        fields = '__all__'

# ViewSets define the view behavior.
class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	



# Serializers define the API representation.
class TratamientoSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Tratamiento
        fields = '__all__'

# ViewSets define the view behavior.
class TratamientoViewSet(viewsets.ModelViewSet):
    queryset = Tratamiento.objects.all()
    serializer_class = TratamientoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	
#///////////////    
# Serializers define the API representation.
class ArticuloSistemaSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = ArticuloSistema
        fields = '__all__'

# ViewSets define the view behavior.
class ArticuloSistemaViewSet(viewsets.ModelViewSet):
    queryset = ArticuloSistema.objects.all()
    serializer_class = ArticuloSistemaSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	


class TratamientoMedicamentoSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = TratamientoMedicamento
        fields = '__all__'

# ViewSets define the view behavior.
class TratamientoMedicamentoViewSet(viewsets.ModelViewSet):
    queryset = TratamientoMedicamento.objects.all()
    serializer_class = TratamientoMedicamentoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]	
