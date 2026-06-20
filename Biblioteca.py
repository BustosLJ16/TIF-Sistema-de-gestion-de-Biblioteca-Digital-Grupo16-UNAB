# Trabajo Integrador Final Grupo N°16 - Sistema de Gestión de Biblioteca Digital.

# Importación de dateTime para registro de Prestamos
from datetime import date, timedelta

# 0. Creación de la MetaClase Mostrar_Info (Para garantizar la renderización de datos)
class mostrarInfo(type):
    def __new__(cls, name, bases, atributos):
        if 'mostrar_info' not in atributos:
            raise TypeError(
                f'La clase: {name} debe tener un método de mostrar_Info() Obligatoriamente.'
            )
        return super().__new__(cls, name, bases, atributos)

# 1. Creación de la Clase Persona y sus Herencias
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
        f"- Email: {self.email}"
    )

class Bibliotecario(Persona):
    def __init__(self, nombre, apellido, legajo, pin):
        super().__init__(nombre, apellido, pin)
        self.legajo= legajo

    def mostrar_info(self):
        return (
        f"{self.nombre} {self.apellido} "
        f"- Legajo: {self.legajo}"
    )

# 2. Creación de la Clase Libro
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
            f"'{self.titulo}' de {self.autor} "
            f"- ISBN: {self.isbn} "
            f"- Año: {self.ano_publicacion}"
        )

# 3. Creación de la Clase Prestamo
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
            f"Fecha devolución: {self.fechaDeDevolucion}"
        )
    
    def mostrar_info(self):
        estado = "Activo" if self.prestamoActivo() else "Devuelto"
        return (
            f"Libro: {self.libro.titulo} | "
            f"Usuario: {self.usuario.nombre} {self.usuario.apellido} | "
            f"Fecha préstamo: {self.fechaDePrestamo} | "
            f"Fecha límite: {self.fechaLimite} | "
            f"Estado: {estado}"
        )


# 4. Creación de la Clase biblioteca
# Mensajes utilizando Decoradores 
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


class Biblioteca():
    _instancia = None  # ← guarda la única instancia

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

    # CRUD DE LIBROS
    def altaLibro(self, libro):
        self.libros.append(libro)
    
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
    
    # CRUD USUARIOS
    def altaUsuario(self, usuario):
        self.usuarios.append(usuario)
        print(f'El usuario "{usuario.nombre} {usuario.apellido}", fue agregado con exito!')

    @mensajeListadoActuales
    def listaUsuariosActuales(self):
        for usuario in self.usuarios:
            print(f"Usuario: {usuario.mostrar_info()}")

    @mensajeListadoActualizado
    def listaUsuariosActualizados(self):
        for usuario in self.usuarios:
            print(f"Usuarios: {usuario.mostrar_info()}")

    def modificarUsuario(self, dni, nuevoNombre=None, nuevoApellido=None, nuevoEmail=None):
        for u in self.usuarios:
            if u.dni == dni:
                u.nombre = nuevoNombre or u.nombre
                u.apellido = nuevoApellido or u.apellido
                u.email = nuevoEmail or u.email
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
    
    # CRUD DE PRESTAMOS
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
        print("Préstamo registrado con éxito.")
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

# PRUEBAS 

# --------  PRUEBAS DE BIBLIOTECA Y CRUD LIBROS -------- 
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
# Listado Actualizado
biblioteca.listaLibrosActualizados()
# Baja de Libros
biblioteca.bajaLibro("1011")
# Listado Final
biblioteca.listaLibrosActualizados()

# -------- PRUEBAS DE BIBLIOTECA Y CRUD LIBROS --------
usuario1 = Usuario("Juan", "Pérez", 12345678, "juan@gmail.com", 1234)
usuario2 = Usuario("María", "Gómez", 87654321, "maria@gmail.com", 1234)
# Alta de usuarios
biblioteca.altaUsuario(usuario1)
biblioteca.altaUsuario(usuario2)
# Listado de usuarios
biblioteca.listaUsuariosActuales()
# Modificacion de datos
biblioteca.modificarUsuario(12345678, nuevoEmail="juanperez@gmail.com")
# Listado Actualizado
biblioteca.listaUsuariosActualizados()
# Baja de Usuario
biblioteca.bajaUsuario(87654321)
# Listado Final
biblioteca.listaLibrosActualizados()

# -------- PRUEBAS DE CRUD PRESTAMOS -------- 
# Registo de Prestamos
biblioteca.registroDePrestamo("123",12345678)
# Lista de Prestamos Activos
biblioteca.listarPrestamosActivos()
# Registo de Prestamos 2
biblioteca.registroDePrestamo("123",87654321)
# Prueba de registro del mismo libro
biblioteca.registroDePrestamo("456",87654321)
# Ver préstamos activos
biblioteca.listarPrestamosActivos()
# Registrar devolución
biblioteca.registrarDevolucion("123")
# Ver préstamos activos luego de la devolución
biblioteca.listarPrestamosActivos()
# Intentar devolver nuevamente
biblioteca.registrarDevolucion("123")
# Libro inexistente
biblioteca.registroDePrestamo("999",12345678)
# Usuario inexistente
biblioteca.registroDePrestamo("123",99999999)


# -------- PRUEBAS DE POLIMORFISMO --------
bibliotecario1 = Bibliotecario("Carlos", "López", "LEG-001", 9876)
bibliotecario2 = Bibliotecario("Ana", "Martínez", "LEG-002", 6789)

print("\n=== DEMOSTRACIÓN DE POLIMORFISMO ===")

elementos = [libro1, libro2, usuario1, bibliotecario1, bibliotecario2]
for e in elementos:
    print(e.mostrar_info())

# Registramos un préstamo nuevo para la demo
biblioteca.registroDePrestamo("123", 12345678)
prestamoDemo = biblioteca.prestamos[-1]  # ← el último registrado

# Mostramos el préstamo ACTIVO
print("\n--- Info de préstamo activo ---")
print(prestamoDemo.mostrar_info())

# Registramos la devolución
biblioteca.registrarDevolucion("123")

# Mostramos el mismo préstamo ahora DEVUELTO
print("\n--- Info de préstamo devuelto ---")
print(prestamoDemo.mostrar_info())

print("\n=== PRUEBA DE SINGLETON ===")
b1 = Biblioteca()
b2 = Biblioteca()
print(b1 is b2)
libro_prueba = Libro("Harry Potter","J.K. Rowling","999",1997,300)
b1.libros.append(libro_prueba)
for libro in b2.libros:
    print(libro.mostrar_info())


def menuUsuario(usuario, biblioteca):
    print(               
        f'-------------------- Menú --------------------\n'
        f'Hola, {usuario.nombre} {usuario.apellido}!\n'
        f'Por favor Indique la opción que desea ejecutar:\n'
        f'1. Prestamo de un Libro.\n'
        f'2. Devolución de un Libro.\n'
        f'3. Modificar un dato de mi cuenta.\n'
        f'0. Salir.\n'
        f'----------------------------------------------')
    opcion=input('Ingrese opción deseada: ')
    while True :
        if opcion == '1':
            print('111')
            break
        elif opcion == '2':
            print('222')
            break
        elif opcion == '3':
            print('333')
            break
        elif opcion == '0':
            print('Hasta Luego!')
            break
        else:
            print(
                f'-------------------- Menú --------------------\n'
                f'Opción NO valida\n'
                f'Por favor Indique la opción que desea ejecutar:\n'
                f'1. Prestamo de un Libro.\n'
                f'2. Devolución de un Libro.\n'
                f'3. Modificar un dato de mi cuenta.\n'
                f'0. Salir.\n'
                f'----------------------------------------------')
            opcion=input('Ingrese opción deseada: ')
# menuUsuario(usuario=usuario1 ,biblioteca='')

def menuBibliotecario(bibliotecario, biblioteca):
    print(               
        f'-------------------- Menú --------------------\n'
        f'Hola, {bibliotecario.nombre} {bibliotecario.apellido} - Legajo N° {bibliotecario.legajo}\n'
        f'Por favor Indique la opción que desea ejecutar:\n'
        f'1. Alta de un Libro.\n'
        f'2. Listado de Libros.\n'
        f'3. Modigicación de un Libro.\n'
        f'4. Baja de un Libro.\n'
        f'5. Prestamos Vigentes.\n'
        f'6. Lista de Usuarios.\n'
        f'7. Baja de Usuarios.\n'
        f'0. Salir.\n'
        f'----------------------------------------------')
    opcion=input('Ingrese opción deseada: ')

    while True:
        if opcion == '1':
            print('111')
            break
        elif opcion == '2':
            print('222')
            break
        elif opcion == '3':
            print('333')
            break
        elif opcion == '4':
            print('444')
            break
        elif opcion == '5':
            print('555')
            break
        elif opcion == '6':
            print('666')
            break
        elif opcion == '7':
            print('777')
            break
        elif opcion == '0':
            print('Hasta Luego!')
            break
        else:
            print(               
                f'-------------------- Menú --------------------\n'
                f'Opción NO Valida\n'
                f'Por favor Indique la opción que desea ejecutar:\n'
                f'1. Alta de un Libro.\n'
                f'2. Listado de Libros.\n'
                f'3. Modigicación de un Libro.\n'
                f'4. Baja de un Libro.\n'
                f'5. Prestamos Vigentes.\n'
                f'6. Lista de Usuarios.\n'
                f'7. Baja de Usuarios.\n'
                f'0. Salir.\n'
                f'----------------------------------------------')
            opcion=input('Ingrese opción deseada: ')
# menuBibliotecario(bibliotecario=bibliotecario1, biblioteca='')

def menuPrincipal():
    print(
        f'-------------------- Menú --------------------\n'
        f'Bienvenido/a a la Biblioteca UNAB\n'
        f'Por favor Indique la opción que desea ejecutar:\n'
        f'1. Iniciar Sesión.\n'
        f'2. Registrarme.\n'
        f'0. Salir.\n'
        f'----------------------------------------------'
    )
    opcion=input('Ingrese opción deseada: ')
    while True:
        if opcion == '1':
            print('Opcion 1')
            break
        elif opcion == '2':
            print(
                f'---------- Registro de Usuario ----------\n'
                f'Por favor, complete los siguientes campos:'
            )
            n=input('Nombre: ')
            a=input('Apellido: ')
            d=int(input('DNI: (Solo Números sin . ni -)'))
            e=input('Email: ')
            p=int(input('Pin: (Solo Números)'))
            nuevoUsuario= Usuario(nombre=n, apellido=a, dni=d, email=e, pin=p)
            biblioteca.altaUsuario(nuevoUsuario)
            break
        elif opcion == '0':
            print ('Hasta Luego!')
            break
        else:
            print(
                f'-------------------- Menú --------------------\n'
                f'Opción NO valida.\n'
                f'Por favor Indique la opción que desea ejecutar:\n'
                f'1. Iniciar Sesión.\n'
                f'2. Registrarme.\n'
                f'0. Salir.\n'
                f'----------------------------------------------'
            )
            opcion=input('Ingrese opción deseada: ')
menuPrincipal()