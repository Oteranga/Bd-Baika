from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Persona, Bicicleta, Punto_acopio, Viaje, Entrega, Donante

#Create a Persona forms
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ('id_persona','dni', 'nombre', 'apellidos', 'celular', 'sexo', 'f_nacimiento', 'correo', 'activo')
        labels = {
            'id_persona': '',
            'dni': '',
            'nombre': '',
            'apellidos': '',
            'celular': '',
            'sexo': '',
            'f_nacimiento': '',
            'correo': '',
            'activo': '',
        }

class BicicletaForm(ModelForm):
    class Meta:
        model = Bicicleta
        fields = '_all_'
        labels = {
            'id_bici': '',
            'marca': '',
            'tipo': '',
            'tamano_aro': '',
            'sexo': '',
            'color': '',
            'estado': '',
            'almacen': '',
            'id_viaje': '',
            'id_entrega': '',
            'id_punto_acopio': '',
            'id_donante': '',
        }

class PuntoAcopioForm(ModelForm):
    class Meta:
        model = Punto_acopio
        fields = '_all_'
        labels = {
            'nombre': '',
            'departamento': '',
            'provincia': '',
            'distrito': '',
            'direccion': '',
        }

class DonanteForm(ModelForm):
    class Meta:
        model = Donante
        fields = '_all_'
        labels = {
            'id_donante': '',
        }

class ViajeForm(ModelForm):
    class Meta:
        model = Viaje
        fields = '_all_'
        labels = {
            'costo': '',
            'tipo_carga': '',
            'ruc_trans': '',
        }

class EntregaForm(ModelForm):
    class Meta:
        model = Entrega
        fields = '_all_'
        labels = {
            'id_viaje': '',
            'fecha': '',
            'id_colegio': '',
        }




