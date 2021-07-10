from django.db import models

# Si blank = true el campo no es necesario
# Si null = true el valor puede ser NULL

# Cambiar todas las ForeignKeys de los hijos de Persona a OneToOneField
# Cambiar los ForeignKeys a ManyToMany o OneToOne como sea necesario de acuerdo al grafico
# Comentar tablas de relacion que ya no sean necesarias

class Persona(models.Model):
    # id_persona = models.CharField(max_length = 8, blank = True, null = False, primary_key = True)
    id_persona = models.CharField(max_length = 8, blank = True, null = False, unique = True)
    dni = models.CharField(max_length = 9, blank = False, null = False)
    nombre = models.CharField(max_length = 255, blank = False, null = False)
    apellidos = models.CharField(max_length = 255, blank = False, null = False)
    celular = models.CharField(max_length = 12, blank = False, null = False)
    sexo = models.CharField(max_length = 1, blank = True, null = True)
    f_nacimiento = models.DateField(blank = True, null = True)
    correo = models.CharField(max_length = 255, blank = False, null = False)
    activo = models.BooleanField(blank = True, null = True)

    def __str__(self):
        return self.nombre

    def edit_id(self):
        self.id_persona = self.nombre[0:2] + self.dni[0:2]

class Colegio(models.Model):
    id_colegio = models.CharField(max_length = 10, blank = True, null = False, primary_key = True)
    nombre = models.CharField(max_length = 255, blank = False, null = False)
    provincia = models.CharField(max_length = 255, blank = False, null = False)
    departamento = models.CharField(max_length = 255, blank = False, null = False)
    distrito = models.CharField(max_length = 255, blank = False, null = False)
    direccion = models.CharField(max_length = 255, blank = False, null = False) 

    def __str__(self):
        return self.nombre

class Beneficiario(models.Model):
    id_beneficiario = models.OneToOneField(Persona, on_delete = models.CASCADE)
    estatura = models.FloatField(blank = False, null = False)
    tiempo_caminata = models.FloatField(blank = False, null = False)
    id_colegio = models.ForeignKey(Colegio, on_delete =  models.CASCADE)

    def __str__(self):
        return self.id_beneficiario.nombre

class Director(models.Model):
    id_director = models.OneToOneField(Persona, on_delete = models.CASCADE)
    id_colegio = models.OneToOneField(Colegio, on_delete = models.CASCADE)

    def __str__(self):
        return self.id_director.nombre

class Viaje(models.Model):
    id = models.CharField(max_length = 8, blank = True, null =  False, primary_key = True)
    costo = models.FloatField(blank = False, null = False)
    tipo_carga = models.CharField(max_length = 100, blank = False, null =  False)
    ruc_trans = models.CharField(max_length = 10, blank =  False, null =  False)

    def __str__(self):
        return self.id

class Voluntario_entrega(models.Model):
    id_voluntario_entrega = models.OneToOneField(Persona, on_delete = models.CASCADE)
    id_viaje = models.ManyToManyField(Viaje)

    def __str__(self):
        return self.id_voluntario_entrega.nombre

class Embajador(models.Model):
    id_embajador = models.OneToOneField(Persona, on_delete =  models.CASCADE)

    def __str__(self):
        return self.id_embajador.nombre

class Punto_acopio(models.Model):
    id = models.CharField(max_length = 8, blank = True, null = False, primary_key = True)
    nombre = models.CharField(max_length = 50, blank = False, null =  False)
    departamento = models.CharField(max_length = 50, blank = False, null = False)
    provincia = models.CharField(max_length = 50, blank = False, null = False)
    distrito = models.CharField(max_length = 50, blank = False, null = False)
    direccion =  models.CharField(max_length = 50, blank = False, null = False)

    def __str__(self):
        return self.nombre

class Responsable_acopio(models.Model):
    id_responsable_acopio = models.OneToOneField(Persona, on_delete = models.CASCADE)
    id_punto_acopio = models.OneToOneField(Punto_acopio, on_delete = models.CASCADE)

    def __str__(self):
        return self.id_responsable_acopio.nombre

class Donante(models.Model):
    id_donante = models.ForeignKey(Persona, on_delete =  models.CASCADE)

    def __str__(self):
        return self.id_donante.nombre

class Voluntario_mantenimiento(models.Model):
    id_voluntario_mantenimiento = models.OneToOneField(Persona, on_delete = models.CASCADE)

class Staff(models.Model):
    id_staff = models.OneToOneField(Persona, on_delete = models.CASCADE)
    area = models.CharField(max_length = 50, blank = False, null = False)
    correo_baika = models.CharField(max_length = 255, blank = True, null = True)

class Socio(models.Model):
    id_socio = models.OneToOneField(Persona, on_delete = models.CASCADE)
    banco = models.CharField(max_length = 100, blank = False, null = False)
    cuenta_banco = models.CharField(max_length = 20, blank = False, null = False)
    monto = models.FloatField(blank = False, null = False)

class Entrega(models.Model):
    id_viaje = models.ForeignKey(Viaje, on_delete = models.CASCADE)
    id = models.CharField(max_length = 8, blank = True, null = False, primary_key = True)
    fecha = models.DateField(blank = False, null = False)
    id_colegio = models.ForeignKey(Colegio, on_delete = models.CASCADE)

class Transportista(models.Model):
    ruc = models.CharField(max_length = 8, blank = False, null = False)
    nombre = models.CharField(max_length = 50, blank = False, null = False)
    correo = models.CharField(max_length = 50, blank = False, null =  False)
    celular = models.CharField(max_length = 15, blank = False, null = False)
    persona_contacto = models.CharField(max_length = 50, blank = False, null = True)
    interprovincial = models.BooleanField(blank = False, null = False)

class Bicicleta(models.Model):
    id_bici = models.CharField(max_length = 8, blank = True, null = False, unique = True)
    marca = models.CharField(max_length = 50, blank = False, null = False)
    tipo = models.CharField(max_length = 50, blank = False, null = False)
    tamano_aro = models.IntegerField(blank = False, null = False)
    sexo = models.CharField(max_length = 1, blank = False, null = False)
    color = models.CharField(max_length = 20, blank = False, null = True)
    estado = models.CharField(max_length = 50, blank = False, null = False)
    almacen = models.BooleanField(blank = False, null = False)
    id_viaje = models.ForeignKey(Viaje, on_delete = models.CASCADE)
    id_entrega = models.ForeignKey(Entrega, on_delete = models.CASCADE)
    id_punto_acopio = models.ForeignKey(Punto_acopio, on_delete = models.CASCADE)
    id_donante = models.ForeignKey(Donante, on_delete = models.CASCADE)

class Herramienta(models.Model):
    id = models.CharField(max_length = 8, blank = True, null = False, primary_key = True)
    nombre = models.CharField(max_length = 50, blank = False, null = False)
    cantidad = models.IntegerField(blank = False, null = False)

class Mantenimiento(models.Model):
    id_man =  models.CharField(max_length = 8, blank = True, null = False)
    fecha = models.DateField(blank = False, null = False)

#Relaciones

# class Col_tiene_dir(models.Model):
#     id_colegio = models.ForeignKey(Colegio, on_delete = models.CASCADE)
#     id_director = models.ForeignKey(Director, on_delete = models.CASCADE)

# class Vol_participa_viaje(models.Model):
#     id_voluntario_entrega = models.ForeignKey(Voluntario_entrega, on_delete = models.CASCADE)
#     id_punto_acopio = models.ForeignKey(Punto_acopio, on_delete = models.CASCADE)

# class Punto_atiende_res(models.Model):
#     id_responsable_acopio = models.ForeignKey(Responsable_acopio, on_delete = models.CASCADE)
#     id_punto_acopio = models.ForeignKey(Punto_acopio, on_delete = models.CASCADE)

class Bici_arregla_herr_man(models.Model):
    id_bicicleta = models.ForeignKey(Bicicleta, on_delete = models.CASCADE)
    id_herramienta = models.ForeignKey(Herramienta, on_delete = models.CASCADE)
    id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete = models.CASCADE)
    parche = models.IntegerField(blank = False, null = True)
    aceite = models.BooleanField(blank = False, null = True)
    grasa = models.BooleanField(blank = False, null = True)
    pedal_cantidad = models.IntegerField(blank = False, null = True)
    cadena = models.IntegerField(blank = False, null = True)
    mango = models.IntegerField(blank = False, null = True)
    taco_freno = models.IntegerField(blank = False, null = True)

# class Vol_ayuda_man(models.Model):
#     id_voluntario_mantenimiento = models.ForeignKey(Voluntario_mantenimiento, on_delete = models.CASCADE)
#     id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete = models.CASCADE)


