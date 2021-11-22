import InterfazConsola as ic
import InterfazGU as iGU
import CRUD
import tkinter as tk 

#inicio
elect = CRUD.Read()

#app
m = iGU.ventanaMenuPrincipal(elect)

#Mainloop
m.mainloop()