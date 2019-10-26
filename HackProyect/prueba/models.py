from django.db import models

# Create your models here.
# Create your models here.
class Pregunta(models.Model):
    descripcion = models.CharField(max_length=200)
    texto = models.CharField(max_length=200)

class Respuesta(models.Model):
	texto = models.CharField(max_length=200)
	pregunta= models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	aplausos = models.IntegerField()

class Doctor(models.Model):
	nombre = models.CharField(max_length=200)
	cedula = models.CharField(max_length=200)
	fecha_Registro = models.DateField()
	AreaEspecialidad = models.CharField(max_length=200)

class Articulo(models.Model):
	"""docstring for Artucilos"""
	fecha_Registro = models.DateField()
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	categoria = models.CharField(max_length=200)
	aplausos = models.IntegerField()
	doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE)
#	likes=models.NumberField()
#/////////// 
class Sintoma(models.Model):
	"""docstring for Articulo_Sintomas"""
	nombre = models.CharField(max_length=200)
	caracteristicas = models.CharField(max_length=200)

class Medicamento(models.Model):
	"""docstring for Articulo_Sintomas"""
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)

class Tratamiento(models.Model):
	"""docstring for Articulo_Sintomas"""
	efectividad = models.IntegerField()
	descripcion = models.CharField(max_length=200)
	fecha_Registro = models.DateField()

class ArticuloSistema(models.Model):
	"""docstring for Articulo_Sintomas"""
	articulo= models.ForeignKey(Articulo, on_delete=models.CASCADE)
	sintomas= models.ForeignKey(Sintoma, on_delete=models.CASCADE)

class TratamientoMedicamento(models.Model):
	"""docstring for Articulo_Sintomas"""
	tratamiento= models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
	medicamentos= models.ForeignKey(Medicamento, on_delete=models.CASCADE)
