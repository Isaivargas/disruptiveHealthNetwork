#from django.contrib import admin


from .models import Pregunta,Respuesta,Doctor,Articulo,Sintoma,Medicamento,Tratamiento,ArticuloSistema,TratamientoMedicamento

admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Doctor)
admin.site.register(Articulo)

admin.site.register(Sintoma)
admin.site.register(Medicamento)
admin.site.register(Tratamiento)
admin.site.register(ArticuloSistema)
admin.site.register(TratamientoMedicamento)


