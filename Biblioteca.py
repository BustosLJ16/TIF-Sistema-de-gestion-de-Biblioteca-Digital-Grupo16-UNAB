# Trabajo Integrador Final Grupo N°16 - Sistema de Gestión de Biblioteca Digital.

#1. Creación de la Clase Persona y sus Herencias
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido= apellido

    def mostrar_info(self):
        return f"{self.nombre} {self.apellido}"

class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido)
        self.dni= dni
        self.email= email

    def mostrar_info(self):
        return f"Usuario: {self.nombre} {self.apellido}"

class Bibliotecario(Persona):
    def __init__(self, nombre, apellido, legajo):
        super().__init__(nombre, apellido)
        self.legajo= legajo
        
    def mostrar_info(self):
        return f"Bibliotecario: {self.nombre} {self.apellido}"

# u= Usuario('Pepe', 'Lopez', 12345678, 'pepe@mail.com')
# print(u.mostrar_info())
# b= Bibliotecario('Marcos', 'Gomez', 32,)
# print(b.mostrar_info())

#2. Creación de la Clase Libro
class Libro ():
    def __init__(self, titulo, autor, isbn, ano_publicacion, cant_paginas):
        self.titulo= titulo
        self.autor= autor
        self.isbn= isbn
        self.ano_publicacion= ano_publicacion
        self.cant_paginas= cant_paginas
    
    def mostrar_libro(self):
        return {
            "Título": self.titulo,
            "Autor": self.autor,
            "Isbn": self.isbn,
            "Año de Publicación": self.ano_publicacion,
            "Cantidad de Páginas": self.cant_paginas
        }

# libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 123, 1943, 120)
# libro2 = Libro("1984", "George Orwell", 456, 1949, 328)
# libro3 = Libro("Don Quijote", "Miguel de Cervantes", 789, 1605, 863)

# biblioteca = [libro1, libro2, libro3]

# for libro in biblioteca:
#     print(libro.mostrar_libro())

