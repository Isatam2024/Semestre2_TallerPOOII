#Crea una clase llamada MainWindow que controle una ventana principal de Tkinter.
#Implementa un método on_close que muestre una ventana emergente con messagebox preguntando si el usuario desea cerrar la ventana.
#Crea una subclase CustomWindow que sobrescriba el método on_close para usar un messagebox diferente (de tipo "yes/no") y confirme si se debe cerrar la ventana.
#Configura la ventana principal para que utilice el método sobrescrito al intentar cerrarse.
#Objetivo: Aplicar sobreescritura de métodos en un entorno interactivo de Tkinter.


import tkinter as tk
from tkinter import messagebox

# Clase principal que maneja la ventana y el método de cierre
class MainWindow(tk.Tk):
    def on_close(self):
        if messagebox.askyesno("Salir", "¿Está seguro de cerrar la ventana?"):
            self.destroy()  # Destruye la ventana

# Subclase que sobrescribe el método on_close con personalización
class CustomWindow(MainWindow):
    def on_close(self):
        if messagebox.askyesno("Confirmación", "¿Seguro que desea cerrar esta ventana personalizada?"):
            self.quit()  # Cierra la aplicación

# Crear la ventana utilizando la subclase CustomWindow
app = CustomWindow()
app.protocol("WM_DELETE_WINDOW", app.on_close)  # Configurar el protocolo de cierre
app.title("Ventana Principal Personalizada")
app.geometry("400x300")

# Iniciar el loop de la aplicación
app.mainloop()
