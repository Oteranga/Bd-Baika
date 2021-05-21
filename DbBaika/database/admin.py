from django.contrib import admin
from .models import Persona, Colegio, Beneficiario, Voluntario_entrega, Embajador

# Register your models here.
admin.site.register(Persona)
admin.site.register(Colegio)
admin.site.register(Beneficiario)
admin.site.register(Voluntario_entrega)
admin.site.register(Embajador)