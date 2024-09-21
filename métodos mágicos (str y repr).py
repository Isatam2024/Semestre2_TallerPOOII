class libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"El título del libro es: {self.titulo}, y su autor es: {self.autor}"
    def __repr__(self):
        return f"Libro(Titulo: {self.titulo}, autor: {self.autor}, paginas: {self.paginas}"
libro1= libro("Cien años de soledad","Gabriel Garcia Marquez",496)
libro2= libro("El principito","Antoine de Saint-Exupéry",120)
print(libro1)
print(libro2)
