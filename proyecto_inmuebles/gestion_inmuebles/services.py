from .models import Inmueble

"""a. Crear un objeto con el modelo.
b. Enlistar desde el modelo de datos.
c. Actualizar un registro en el modelo de datos.
d. Borrar un registro del modelo de datos utilizando un modelo Django"""

def crear_inmueble(nombre, descripcion, m2_construidos, habitaciones, m2_totales, estacionamientos, banos, direccion, id_comuna, tipo_inmueble, precio_mensual, id_dueno):

    Inmueble(nombre=nombre, direccion=direccion, descripcion=descripcion, m2_construidos=m2_construidos, m2_totales=m2_totales, estacionamientos=estacionamientos, habitaciones=habitaciones, banos=banos, comuna_id=id_comuna, tipo_inmueble=tipo_inmueble, precio_mensual=precio_mensual, dueno_id=id_dueno).save()

    
    

def listar_inmuebles():

    return Inmueble.objects.all()
    ...

def actualizar_registro(id:int, descripcion:str):
    inmueble_object = Inmueble.objects.get(id=id)
    inmueble_object.descripcion = descripcion
    inmueble_object.save()

def borrar_registro(id:int):
    inmueble_object = Inmueble.objects.get(id=id)
    inmueble_object.delete()

"""crear_inmueble(
    nombre="Depto1",
    descripcion="Descripción fea",
    m2_construidos=48, 
    habitaciones=3,
    m2_totales=80,
    estacionamientos=0,
    banos=2,
    direccion="calle falsa #12",
    id_comuna=1,
    tipo_inmueble="departamento",
    precio_mensual=30,
    id_dueno=1)"""