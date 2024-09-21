from abc import ABC, abstractmethod

class Publicacion(ABC):
    @abstractmethod
    def informacion(self):
        pass

    @abstractmethod
    def resumen(self):
        pass

class libro(Publicacion):
    def informacion(self):
        return "Este es un libro"

    def resumen(self):
        super(libro, self).resumen()
        return "Este libro tiene un resumen breve"
class Revista(Publicacion):
    def informacion(self):
        return "Esta es una revista"

    def resumen(self):
        return "Este resumen es breve"

r =Revista()
r.informacion()
r.resumen()

l = libro()
l.informacion()
l.resumen()
print (r.informacion())
print(r.resumen())
print (l.informacion())
print(l.resumen())
