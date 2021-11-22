#librerias de la interfaz grafica 
import tkinter as tk
import InterfazConsola as ic


#Logica para hacer consultas 
import CRUD

#Contrutir ventana principal de la app
def ventanaMenuPrincipal(elect):

    #Creamos nuestra ventana principal
    m = tk.Tk()
    m.title("App Crud listado de Electrodomesticos")

    btnListarTareas = tk.Button(m,text='Listar Electrodomesticos',command = lambda : ic.mostrartareas(elect))
    btnListarTareas.pack()

    #Campo para escribir texto 

    etID = tk.Label(m,text='Id:')
    etID.pack()
    entradaID = tk.Entry(m)
    entradaID.pack()

    etNombre = tk.Label(m,text='Nombre:')
    etNombre.pack()
    entradaNombre = tk.Entry(m)
    entradaNombre.pack()

    etMarca = tk.Label(m,text='Marca:')
    etMarca.pack()
    entradaMarca = tk.Entry(m)
    entradaMarca.pack()

    etConsumo = tk.Label(m,text='Consumo:')
    etConsumo.pack()
    entradaConsumo = tk.Entry(m)
    entradaConsumo.pack()

    etHabitacion = tk.Label(m,text='Habitacion:')
    etHabitacion.pack()
    entradaHabitacion = tk.Entry(m)
    entradaHabitacion.pack()

    #funcion que recoge la informacion de los campos del formulario 
    def adicionarElectrodomestico():
        id = entradaID.get()
        if id in elect.keys() :
            print("ID: " + id + " ya existe")
            return
        elet = {
                'id':int(entradaID.get()),
                'nombre':entradaNombre.get(),
                'marca':entradaMarca.get(),
                'consumo':int(entradaConsumo.get()),
                'habitacion':entradaHabitacion.get(),
            }

        CRUD.Create(id,elet,elect)

    btnAdicionarElectrodomestico = tk.Button(m,text='Adicionar Electrodomestico',command = adicionarElectrodomestico)
    btnAdicionarElectrodomestico.pack()

    def eliminar():
        id = entradaID.get()
        CRUD.Eliminar(id, elect)
        
    #boton Eliminar
    btnEliminar = tk.Button(m,text='Eliminar ',command = eliminar)
    btnEliminar.pack()
    
    def consumomax():
        electrodomesticos = []
        for k,v in elect.items(): electrodomesticos.append(v)
        max_consumo = max(electrodomesticos, key= lambda x : x['consumo'])
        min_consumo = min(electrodomesticos, key= lambda x : x['consumo'])
        print("Consumo Maximo: " + str(max_consumo['consumo']) + ", Nombre electrodomestico: " + max_consumo['nombre']) 
        print("Consumo Minimo: " + str(min_consumo['consumo']) + ", Nombre electrodomestico: " + min_consumo['nombre']) 

    #boton 
    btnConsumoMaxMin = tk.Button(m,text='Consumo max y consumo min ',command = consumomax)
    btnConsumoMaxMin.pack()
            
    def Consumototal():
        sumatotalconsumo = 0
        for k,v in elect.items(): sumatotalconsumo+=v['consumo']
        print('consumototal')
        print(sumatotalconsumo)

    #boton 
    btnConsumoTotal = tk.Button(m,text='Consumo total',command = Consumototal)
    btnConsumoTotal.pack()

    return m