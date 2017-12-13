#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
from json import loads
from json import dump


def cargaDatos():
	person = {}
	
	person["Nombre"]= sd.askstring("Información", "Ingrese su nombre")
	person["Apellido"]= sd.askstring("Información", "Ingrese su apellido")
	person["Telefono"]= sd.askstring("Información", "Ingrese su N° de Telefono")
	
	with open("persona.json", "w") as fileOut:
		dump(person, fileOut)
		
def showData():
	vertical = 80
	
	person = loads(open("persona.json").read())

	for key, value in person.items():
		dataLanbel = tk.Label(mainForm, text = key + ": " + value)
		dataLanbel.place(x = 10, y = vertical)
		vertical +=20
	
mainForm = tk.Tk()
mainForm.title("Ejercicio tkinter")
mainForm.geometry("600x200")

cargarButton = tk.Button(mainForm, text = "Cargar personas", command = cargaDatos)
cargarButton.place(x = 10, y = 10)

mensajesButton = tk.Button(mainForm, text = "Contactos", command = showData)
mensajesButton.place(x = 160, y = 10)


mainForm.mainloop()
