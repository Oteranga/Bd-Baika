from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bici_arregla_herr_man, Bicicleta, Donante, Entrega, Herramienta, Mantenimiento, Persona, Colegio, Beneficiario, Punto_acopio, Responsable_acopio, Socio, Staff, Transportista, Voluntario_entrega, Embajador, Director, Viaje, Voluntario_mantenimiento, Punto_acopio, Responsable_acopio, Donante, Voluntario_mantenimiento, Staff, Socio, Entrega, Transportista, Bicicleta, Herramienta, Mantenimiento, Bici_arregla_herr_man
from .forms import PersonaForm

def delete_person(request, person_id):
    person = Persona.objects.get(pk = person_id)
    person.delete()
    return redirect('list-people')

def update_person(request, person_id):
    person = Persona.objects.get(pk = person_id)
    form = PersonaForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save
        return redirect('list-people')
    return render(request, 'update_person.html', {'person': person, 'form': form})

def show_person(request, person_id):
    person = Persona.objects.get(pk = person_id)
    return render(request, 'show_person.html', {'person': person})

def list_people(request):
    people_list = Persona.objects.all()
    return render(request, 'show_people.html', {'people_list': people_list})

def add_person(request):
    submitted = False
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_person?submitted = True')
    else:
        form = PersonaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_person.html', {'form': form, 'submitted':submitted})

def home(request):
    return render(request, 'home.html', {})

def all_people(request):
    people_list = Persona.objects.all()
    return render(request, 'people.html', {'people_list': people_list})

