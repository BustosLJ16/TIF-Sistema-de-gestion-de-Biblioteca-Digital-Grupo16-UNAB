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

#3. Creación de la Clase biblioteca
class Biblioteca():
    def __init__(self):
        self.libros= []

    def altaLibro(self, libro):
        self.libros.append(libro)
    
    def listaLibrosActuales(self):
        print('------------ Nuestros Libros Actuales----------')
        for libro in self.libros:
            print(f"Libro: ${libro.mostrar_libro()}")

    def listaLibrosActualizados(self):
        print('------------ Nuestros Libros Actualizados----------')
        for libro in self.libros:
            print(f"Libro: ${libro.mostrar_libro()}")

    def modificarLibro(self, isbn, tituloNuevo=None, autorNuevo=None):
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.titulo = tituloNuevo or libro.titulo
                libro.autor = autorNuevo or libro.autor
                return True
        return False
    
    def baja(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                return True
        return False

# PRUEBAS DE BIBLIOTECA Y CRUD LIBROS
biblioteca = Biblioteca()

libro1 = Libro("Harry Potter", "J.K. Rowling", "123", 1997, 300)
libro2 = Libro("El Hobbit", "Tolkien", "456", 1937, 310)
libro3 = Libro("El libro troll", "El Rubius", "789", 2014, 310)
libro4 = Libro("Lyna Familia anormal", "Lyna Vallejos", "1011", 2018, 310)

# Alta de Libros
biblioteca.altaLibro(libro1)
biblioteca.altaLibro(libro2)
biblioteca.altaLibro(libro3)
biblioteca.altaLibro(libro4)

# Listado
biblioteca.listaLibrosActuales()

# Modificacion de datos
biblioteca.modificarLibro("123", tituloNuevo="Harry Potter 2")

# Listado Final
biblioteca.listaLibrosActualizados()

# Baja de Libros
biblioteca.baja("1011")

# Listado Final
biblioteca.listaLibrosActualizados()

# PRUEBAS DE USUARIO
# u= Usuario('Pepe', 'Lopez', 12345678, 'pepe@mail.com')
# print(u.mostrar_info())
# b= Bibliotecario('Marcos', 'Gomez', 32,)
# print(b.mostrar_info())