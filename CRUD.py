#Libreria
import json

#Capa logica

#Create adicionar tareas
def Create(id,elet,elect):
    elect[id] = elet
    # persistencia de datos
    # escribir el diccionario de electrodomesticos en memoria al archivo
    Write(elect)
    
# Eliminar una entrada
def Eliminar(id,elect):
    try:
        del elect[id]
        Write(elect)
    except:
        print('ERROR: ID no existe')
#Read
def Read():
    # inicializacion
    # se abre el archivo data.json para procesar los datos
    fichero = open("data.json")
    # Se lee el contenido del archivo. esto devuelve un string
    contenido = fichero.read()
    # se transforma el string a un Diccionario de PYthon para poderlo trabajar
    data = json.loads(contenido)
    return data

def Write(data):
    with open('data.json','w') as fichero:
        json.dump(data, fichero)
    