from abc import ABC, abstractmethod


class Publicacion(ABC):

    @abstractmethod
    def informacion(self):
        pass

    @abstractmethod
    def resumen(self):
        pass

    def __init__(self, informacion, resumen):
        self._informacion = informacion
        self._resumen = resumen

    def __str__(self):
        return f"{self.informacion()}, {self.resumen()}"


class Libro(Publicacion):
    def __init__(self, informacion, resumen):
        super().__init__(informacion, resumen)

    def informacion(self):
        return f"Este es un libro: {self._informacion}"

    def resumen(self):
        return f"Resumen del libro: {self._resumen}"


class Revista(Publicacion):
    def __init__(self, informacion, resumen):
        super().__init__(informacion, resumen)

    def informacion(self):
        return f"Esta es una revista: {self._informacion}"

    def resumen(self):
        return f"Resumen de la revista: {self._resumen}"


# Crear instancias de Revista y Libro con los parámetros correctos
revista1 = Revista("Revista de Moda", "Lo último en tendencias de moda")
libro1 = Libro("El amor en la noche", "Una historia de amor en la noche")

# Imprimir información y resumen de las instancias
print(revista1)
print(libro1)
