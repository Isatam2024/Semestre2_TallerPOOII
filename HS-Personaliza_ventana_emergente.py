#Crea una clase base llamada PopupBase que reciba un mensaje y lo muestre usando un messagebox de tipo "info" en Tkinter.
#Luego, crea una clase hija llamada CustomPopup que sobrescriba el método que muestra el mensaje, cambiando el título y personalizando el contenido del mensaje.
#Crea una instancia de la clase hija y muéstrala.
#Objetivo: Implementar herencia simple y sobrescritura de métodos.


import tkinter as tk
from tkinter import messagebox

# Primero debemos crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de PopupBase")

# Luego se crea la clase PopubBase  propuesta en el ejercicio de la clase
class PopupBase:
    def click(self):
        messagebox.showinfo("Mensaje informativo", "Bienvenido")
#Luego se crea la clase hija custompopup
class CustomPopup(PopupBase):
    def click(self):
        messagebox.showinfo("Mensaje personalizado", "Felicitaciones")

# se crea instancia para la clase principal
popup = PopupBase()

# Se crea una instancia de la clase hija
custom_popup = CustomPopup()

#Se crea  el botón y asociarlo al método click de la instancia popup
button = tk.Button(root, text="Click", command=popup.click)
button.pack(pady=10)

# Se crea otro botón y asociarlo al método click de la instancia de la clase hija
custom_button = tk.Button(root, text="Click personalizado", command=custom_popup.click)
custom_button.pack(pady=10)

# Iniciar el loop de la ventana
root.mainloop()


