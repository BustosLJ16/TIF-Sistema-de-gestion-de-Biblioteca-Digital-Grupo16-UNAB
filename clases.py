# Importación de "dateTime" para los Registros de Prestamos
from datetime import date, timedelta

# -------------------- MetaClase --------------------
# MetaClase Mostrar_Info (Para garantizar la renderización de datos)
class mostrarInfo(type):
    def __new__(cls, name, bases, atributos):
        if 'mostrar_info' not in atributos:
            raise TypeError(
                f'La clase: {name} debe tener un método de mostrar_Info() Obligatoriamente.'
            )
        return super().__new__(cls, name, bases, atributos)


# -------------------- Clase Persona y sus Herencias --------------------
class Persona(metaclass=mostrarInfo):
    def __init__(self, nombre, apellido, pin):
        self.nombre= nombre
        self.apellido= apellido
        self.pin= pin

    def mostrar_info(self):
        return (f'{self.nombre} {self.apellido}')

class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, email, pin):
        super().__init__(nombre, apellido, pin)
        self.dni= dni
        self.email= email

    def mostrar_info(self):
        return (
        f"{self.nombre} {self.apellido} "
        f"- DNI: {self.dni} "
        f"- Email: {self.email}")

class Bibliotecario(Persona):
    def __init__(self, nombre, apellido, legajo, pin):
        super().__init__(nombre, apellido, pin)
        self.legajo= legajo

    def mostrar_info(self):
        return (
        f"Bibliotecario: {self.nombre} {self.apellido} "
        f"- Legajo: {self.legajo}")

# -------------------- Clase Libro --------------------
class Libro (metaclass=mostrarInfo):
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
    
    def mostrar_info(self):
        return (
            f"Libro: '{self.titulo}' de {self.autor} "
            f"- ISBN: {self.isbn} "
            f"- Año: {self.ano_publicacion}")

# -------------------- Clase Prestamo --------------------
class Prestamo(metaclass=mostrarInfo):
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fechaDePrestamo= date.today()
        self.fechaLimite = date.today() + timedelta(days=90)
        self.fechaDeDevolucion= None
    
    def devolucion(self):
        self.fechaDeDevolucion= date.today()

    def prestamoActivo(self):
        return self.fechaDeDevolucion is None
    
    def mostrarInfoPrestamo(self):
        return (
            f"Libro: {self.libro.titulo} | "
            f"Usuario: {self.usuario.nombre} {self.usuario.apellido} | "
            f"Fecha préstamo: {self.fechaDePrestamo} | "
            f"Fecha límite: {self.fechaLimite} | "
            f"Fecha devolución: {self.fechaDeDevolucion}")
    
    def mostrar_info(self):
        estado = "Activo" if self.prestamoActivo() else "Devuelto"
        return (
            f"Libro: {self.libro.titulo} | "
            f"Usuario: {self.usuario.nombre} {self.usuario.apellido} | "
            f"Fecha préstamo: {self.fechaDePrestamo} | "
            f"Fecha límite: {self.fechaLimite} | "
            f"Estado: {estado}")

# -------------------- Decoradores --------------------
def mensajeListadoActuales(func):
    def wrapped(*args, **kwargs):
        print("=== Datos Actuales ===")
        return func(*args, **kwargs)
    return wrapped

def mensajeListadoActualizado(func):
    def wrapped(*args, **kwargs):
        print("=== Datos Actualizados ===")
        return func(*args, **kwargs)
    return wrapped

# -------------------- Clase Biblioteca --------------------
class Biblioteca():
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self):
        if getattr(self, "_inicializado", False):
            return

        self.libros = []
        self.usuarios = []
        self.prestamos = []
        self.bibliotecarios= []
        self._inicializado = True

    # -------------------- CRUD de Libros --------------------
    def altaLibro(self, libro):
        for l in self.libros:
            if l.isbn == libro.isbn:
                print(f'Ya existe un libro con el ISBN {libro.isbn}.')
                return False

        self.libros.append(libro)
        print(f'El libro "{libro.titulo}" fue registrado con éxito.')
        return True
    
    @mensajeListadoActuales
    def listaLibrosActuales(self):
        for libro in self.libros:
            print(f"Libro: {libro.mostrar_libro()}")

    @mensajeListadoActualizado
    def listaLibrosActualizados(self):
        for libro in self.libros:
            print(f"Libro: {libro.mostrar_libro()}")

    def modificarLibro(self, isbn, tituloNuevo=None, autorNuevo=None):
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.titulo = tituloNuevo or libro.titulo
                libro.autor = autorNuevo or libro.autor
                print(f'El libro con ID:"{libro.isbn}" fue Modificado con Éxito!')
                return True
        return False
    
    def bajaLibro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                print(f'El libro con ID:"{libro.isbn}" fue eliminado con Éxito!')
                return True
        return False
    
    # -------------------- CRUD de Usuario --------------------
    def altaUsuario(self, usuario):
        for u in self.usuarios:
            if u.dni == usuario.dni:
                print(f'Ya existe un usuario con el DNI {usuario.dni}.')
                return False

            if u.email == usuario.email:
                print(f'Ya existe un usuario con el email {usuario.email}.')
                return False

        self.usuarios.append(usuario)
        print(
            f'El usuario "{usuario.nombre} {usuario.apellido}" '
            f'fue agregado con éxito!')
        return True

    @mensajeListadoActuales
    def listaUsuariosActuales(self):
        for usuario in self.usuarios:
            print(f"Usuario: {usuario.mostrar_info()}")

    @mensajeListadoActualizado
    def listaUsuariosActualizados(self):
        for usuario in self.usuarios:
            print(f"Usuario: {usuario.mostrar_info()}")

    def modificarUsuario(self, dni, nuevoNombre=None, nuevoApellido=None, nuevoEmail=None, nuevoPin=None):
        for u in self.usuarios:
            if u.dni == dni:
                u.nombre = nuevoNombre or u.nombre
                u.apellido = nuevoApellido or u.apellido
                u.email = nuevoEmail or u.email
                u.pin = nuevoPin or u.pin
                print(f'El usuario con DNI "{dni}" fue modificado con éxito.')
                return True
        return False
    
    def bajaUsuario(self,dni):
        for u in self.usuarios:
            if u.dni == dni:
                self.usuarios.remove(u)
                print(f'El usuario con DNI "{dni}" fue eliminado con éxito.')
                return True
        return False
    
    # -------------------- CRUD de Bibliotecarios --------------------
    def altaBibliotecario(self, bibliotecario):
        for b in self.bibliotecarios:
            if b.legajo == bibliotecario.legajo:
                print(
                    f'Ya existe un bibliotecario con el legajo '
                    f'{bibliotecario.legajo}.')
                return False

        self.bibliotecarios.append(bibliotecario)
        print(
            f'El bibliotecario "{bibliotecario.nombre} '
            f'{bibliotecario.apellido}" fue agregado con éxito!')
        return True
    
    @mensajeListadoActuales
    def listaBibliotecariosActuales(self):
        for bibliotecario in self.bibliotecarios:
            print(
            f"Bibliotecario: {bibliotecario.mostrar_info()}")

    def bajaBibliotecario(self, legajo):
        for b in self.bibliotecarios:
            if b.legajo  == 'LEG-'+str(legajo):
                self.bibliotecarios.remove(b)
                print(
                    f'El bibliotecario con legajo "{legajo}" fue eliminado con éxito.')
                return True
        return False

    # -------------------- CRUD de Prestamos --------------------
    def registroDePrestamo(self, isbn, dni):
        libroEncontrado= None
        for l in self.libros:
            if l.isbn == isbn:
                libroEncontrado = l 
                break

        usuarioEncontrado= None
        for u in self.usuarios:
            if u.dni == dni:
                usuarioEncontrado= u
                break

        if libroEncontrado is None:
                print("Libro no encontrado.")
                return False

        if usuarioEncontrado is None:
            print("Usuario no encontrado.")
            return False

        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn and prestamo.prestamoActivo():
                print("El libro ya está prestado.")
                return False

        nuevoPrestamo = Prestamo(libroEncontrado, usuarioEncontrado)
        self.prestamos.append(nuevoPrestamo)
        print(
            f"Préstamo del libro '{libroEncontrado.titulo}' fue registrado con éxito.\n"
            f"Fecha préstamo: {nuevoPrestamo.fechaDePrestamo} "
            f"- Fecha límite: {nuevoPrestamo.fechaLimite}")
        return True
    
    def registrarDevolucion(self,isbn):
        for p in self.prestamos:
            if p.libro.isbn == isbn and p.prestamoActivo():
                p.devolucion()
                print("Devolución registrada con éxito.")
                return True

        print("No existe préstamo activo para ese libro.")
        return False
            
    def listarPrestamosActivos(self):
        print("=== PRÉSTAMOS ACTIVOS ===")
        hay_prestamos = False

        for p in self.prestamos:
            if p.prestamoActivo():
                print(p.mostrarInfoPrestamo())
                hay_prestamos = True

        if not hay_prestamos:
            print("No hay préstamos activos.")