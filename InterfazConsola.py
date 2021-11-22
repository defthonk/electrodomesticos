#Logica para hacer consultas 
import CRUD

#Interaccion 
def menuprincipal():
    print("Elija una opcion")
    print("1. Adicionar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    opcion = int(input('Ingresar opcion'))
    return opcion

def formularioCrearTarea():
    id = input('ingresar id: ')
    nombre = input('ingrese nombre: ')
    marca = input('ingrese marca: ')
    consumo = input('ingrese cosumo: ')
    habitacion = input('ingresar habitacion: ')
    elet = {
                'id':id,
                'nombre':nombre,
                'marca':marca,
                'consumo':consumo,
                'habitacion':habitacion

            }
    return id,elet

def mostrartareas(elect): 
    print('listado tareas')
    for id ,elect1 in elect.items():
        print(f"{id} - {elect1['id']}, {elect1['nombre']}, {elect1['marca']}, {elect1['consumo']}, {elect1['habitacion']} ")

def mensajeCierre(if1):
    print()
    print(if1)
    print()