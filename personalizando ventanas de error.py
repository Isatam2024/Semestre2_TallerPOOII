#Crea una clase base llamada ErrorPopup que muestre un mensaje de error usando messagebox.
#Crea una clase hija llamada CustomErrorPopup que sobrescriba el método que muestra el mensaje de error, personalizando tanto el título como el contenido del mensaje.
#Crea una instancia de la clase hija y usa el método sobrescrito.
#Objetivo: Practicar la sobreescritura de métodos.

import tkinter as tk
from tkinter import messagebox

class ErrorPopup:
    def show_error(self):
        messagebox.showerror("Error", "Ha ocurrido un error.")
class CustomErrorPopup(ErrorPopup):
    def show_error(self):
        messagebox.showerror("Error Personalizado", "Ha ocurrido un error en la aplicación. Por favor, contacte con el administrador.")


root = tk.Tk()
root.withdraw()
ErrPopup = ErrorPopup()
CustomErrPopup = CustomErrorPopup()

ErrPopup.show_error()
CustomErrPopup.show_error()

root.mainloop()
