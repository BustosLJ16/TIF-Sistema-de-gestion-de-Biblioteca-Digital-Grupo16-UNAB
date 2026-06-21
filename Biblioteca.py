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
    
    # CRUD BIBLIOTECARIOS
    def altaBibliotecario(self, bibliotecario):
        self.bibliotecarios.append(bibliotecario)
        print(
        f'El bibliotecario "{bibliotecario.nombre} {bibliotecario.apellido}" fue agregado con éxito!')

    @mensajeListadoActuales
    def listaBibliotecariosActuales(self):
        for bibliotecario in self.bibliotecarios:
            print(
            f"Bibliotecario: {bibliotecario.mostrar_info()}")

    def bajaBibliotecario(self, legajo):
        for b in self.bibliotecarios:
            if b.legajo == legajo:
                self.bibliotecarios.remove(b)
                print(
                    f'El bibliotecario con legajo "{legajo}" fue eliminado con éxito.')
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


biblioteca=Biblioteca()

libro1 = Libro("Harry Potter", "J.K. Rowling", "123", 1997, 300)
biblioteca.altaLibro(libro1)
libro2 = Libro("Harry Potter", "J.K. Rowling", "999", 1997, 300)
biblioteca.altaLibro(libro2)

usuario1 = Usuario("Juan", "Pérez", 12345678, "juan@gmail.com", 1234)
usuario2 = Usuario("María", "Gómez", 87654321, "maria@gmail.com", 4321)

biblioteca.altaUsuario(usuario1)
biblioteca.altaUsuario(usuario2)

biblioteca.listaUsuariosActuales()

bibliotecario01 = Bibliotecario("Susana", "Gutierrez", "LEG-821", 5678)
bibliotecario02 = Bibliotecario("Luciano", "Castro", "LEG-301", 5678)

biblioteca.altaBibliotecario(bibliotecario01)
biblioteca.altaBibliotecario(bibliotecario02)

biblioteca.registroDePrestamo("123",12345678)
biblioteca.registroDePrestamo("123",87654321)
biblioteca.listarPrestamosActivos()

# ------------------------------ FUNCIONES USUARIO ------------------------------
def usuarioHacerPrestamo(usuario, biblioteca):
    print(
        f'---------- Registrar Prestamo ----------\n'
        f'Por favor, complete los siguientes campos:')
    d= int(input('DNI (Solo Números sin . ni -): '))
    i= input("Ingrese ISBN del libro: ")
    if usuario.dni == d:
        biblioteca.registroDePrestamo(
            i, usuario.dni)
    else:
        print('Los Datos son Incorrectos. Intente Nuevamente')
        usuarioHacerPrestamo()

def usuarioDevolucionPrestamo(usuario, biblioteca):
    print(
        f'---------- Registrar Prestamo ----------\n'
        f'Por favor, complete los siguientes campos:')
    d= int(input('DNI (Solo Números sin . ni -): '))
    i= input("Ingrese ISBN del libro: ")

    if usuario.dni == d:
        biblioteca.registrarDevolucion(i)
        print("Devolución registrada correctamente.")
    else:
        print('Los Datos son Incorrectos. Intente Nuevamente')
        usuarioDevolucionPrestamo()

def usuarioModificarCuenta(usuario, biblioteca):
    print(
        f'---------- Modificar Cuenta ----------\n'
        f'Por favor, complete los siguientes campos - Deje vacío el dato que no quiera modificar: ')
    d= int(input('DNI (Solo Números sin . ni -): '))
    nn= input('Ingrese Nuevo Nombre: ')
    na= input('Ingrese Nuevo Apellido: ')
    ne= input('Ingrese Nuevo Email: ')
    np= input('Ingrese Nuevo Pin (Solo Número): ')
    if usuario.dni == d:
        biblioteca.modificarUsuario(
            usuario.dni,
            nn if nn else None,
            na if na else None,
            ne if ne else None,
            np if np else None
        )
    else:
        print('Las Credenciales son Incorrectas. Intente Nuevamente.')
        usuarioModificarCuenta(usuario, biblioteca)
# ------------------------------ MENÚ USUARIO ------------------------------
def menuUsuario(usuario, biblioteca):
    print(               
        f'-------------------- Menú --------------------\n'
        f'Hola, {usuario.nombre} {usuario.apellido}!\n'
        f'Por favor Indique la opción que desea ejecutar:\n'
        f'1. Lista de Libros Actuales.\n'
        f'2. Prestamo de un Libro.\n'
        f'3. Devolución de un Libro.\n'
        f'4. Modificar un dato de mi cuenta.\n'
        f'0. Salir.\n'
        f'----------------------------------------------')
    opcion=input('Ingrese opción deseada: ')
    while True :
        if opcion == '1':
            biblioteca.listaLibrosActuales()
            break
        elif opcion == '2':
            usuarioHacerPrestamo(usuario, biblioteca)
            break
        elif opcion == '3':
            usuarioDevolucionPrestamo(usuario, biblioteca)
            break
        elif opcion == '4':
            usuarioModificarCuenta(usuario, biblioteca)
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

# ------------------------------ FUNCIONES BIBLIOTECARIO ------------------------------
def bibliotecarioAltaLibro(bibliotecario, biblioteca):
    print(
        f'---------- Registrar Libro Nuevo ----------\n'
        f'Por favor, complete los siguientes campos:')
    l=int(input('Ingrese su N° de Legajo: '))
    if bibliotecario.legajo == 'LEG-'+str(l):
        t=input('Ingrese el Título: ')
        a=input('Ingrese el Autor: ')
        i=input('Ingrese el ISBN: ')
        ap= int(input('Ingrese el Año de Publicación: '))
        p= int(input('Ingrese la Cantidad de Páginas: '))
        libro= Libro(t,a,i,ap,p)
        biblioteca.altaLibro(libro)
    else:
        print('Los Datos son Incorrectos. Intente Nuevamente.')
        bibliotecarioAltaLibro(bibliotecario, biblioteca)

def bibliotecarioModificarLibro(bibliotecario, biblioteca):
    print(
        f'---------- Modificar Libro  ----------\n'
        f'Por favor, complete los siguientes campos - Deje vacío el dato que no quiera modificar: ')
    l=int(input('Ingrese su N° de Legajo: '))
    if bibliotecario.legajo == 'LEG-'+str(l):
        i= input('Ingrese ISBN del libro: ')
        nt= input('Ingrese el Nuevo Título: ')
        na= input('Ingrese el Nuevo Autor: ')
        biblioteca.modificarLibro(
            i,
            nt if nt else None,
            na if na else None
        )
    else:
        print('Los Datos son Incorrectos. Intente Nuevamente.')
        bibliotecarioModificarLibro(bibliotecario, biblioteca)

def bibliotecarioBajaLibro(bibliotecario, biblioteca):
    print(
        f'---------- Dar de Baja un Libro ----------\n'
        f'Por favor, complete los siguientes campos:')
    l=int(input('Ingrese su N° de Legajo: '))
    if bibliotecario.legajo == 'LEG-'+str(l):
        i= input('Ingrese ISBN del libro: ')
        biblioteca.bajaLibro(i)
    else:
        print('Los Datos son Incorrectos. Intente Nuevamente.')
        bibliotecarioBajaLibro(bibliotecario, biblioteca)

def bibliotecarioBajaUsuarios(bibliotecario, biblioteca):
    print(
        f'---------- Dar de Baja Un Usuario ----------\n'
        f'Por favor, complete los siguientes campos:')
    l=int(input('Ingrese su N° de Legajo: '))
    if bibliotecario.legajo == 'LEG-'+str(l):
        d= int(input('DNI del Usuario (Solo Números sin . ni -): '))
        biblioteca.bajaUsuario(d)
    else:
        print('Los Datos son Incorrectos. Intente Nuevamente.')
        bibliotecarioBajaUsuarios(bibliotecario, biblioteca)

# ------------------------------ MENÚ BIBLIOTECARIO ------------------------------
def menuBibliotecario(bibliotecario, biblioteca):
    print(               
        f'-------------------- Menú --------------------\n'
        f'Hola, {bibliotecario.nombre} {bibliotecario.apellido} - Legajo N° {bibliotecario.legajo}\n'
        f'Por favor Indique la opción que desea ejecutar:\n'
        f'1. Alta de un Libro.\n'
        f'2. Listado de Libros.\n'
        f'3. Modificación de un Libro.\n'
        f'4. Baja de un Libro.\n'
        f'5. Prestamos Vigentes.\n'
        f'6. Lista de Usuarios.\n'
        f'7. Baja de Usuarios.\n'
        f'0. Salir.\n'
        f'----------------------------------------------')
    opcion=input('Ingrese opción deseada: ')

    while True:
        if opcion == '1':
            bibliotecarioAltaLibro(bibliotecario, biblioteca)
            break
        elif opcion == '2':
            biblioteca.listaLibrosActuales()
            break
        elif opcion == '3':
            bibliotecarioModificarLibro(bibliotecario,biblioteca)
            break
        elif opcion == '4':
            bibliotecarioBajaLibro(bibliotecario, biblioteca)
            break
        elif opcion == '5':
            biblioteca.listarPrestamosActivos()
            break
        elif opcion == '6':
            biblioteca.listaUsuariosActuales()
            break
        elif opcion == '7':
            bibliotecarioBajaUsuarios(bibliotecario,biblioteca)
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

# ------------------------------ MENÚ INICIO SESION / REGISTRO ------------------------------
def menuRegistroUsuario():
    print(
        f'---------- Registro de Usuario ----------\n'
        f'Por favor, complete los siguientes campos:')
    n=input('Nombre: ')
    a=input('Apellido: ')
    d=int(input('DNI (Solo Números sin . ni -): '))
    e=input('Email: ')
    p=int(input('Pin (Solo Números): '))
    nuevoUsuario= Usuario(nombre=n, apellido=a, dni=d, email=e, pin=p)
    biblioteca.altaUsuario(nuevoUsuario)
    return nuevoUsuario

def menuSesionUsuario():
    print(
    f'---------- Inicio de Sesión ----------\n'
    f'Por favor, Brinde estos datos:\n')
    d=int(input('Su DNI (Sin . ni -): '))
    p=int(input('Pin (Solo Números): '))
    for u in biblioteca.usuarios:
        if u.dni == d and u.pin == p:
            menuUsuario(u, biblioteca)
            return
    print(
    f'---------- Datos Incorrectos, vuelva a intentarlo ----------\n')
    menuSesionUsuario()

def menuSesionBibliotecario():
    print(
    f'---------- Inicio de Sesión ----------\n'
    f'Por favor, Brinde estos datos:')
    l=int(input('Su N° de Legajo: '))
    p=int(input('Pin (Solo Números): '))
    for b in biblioteca.bibliotecarios:
        if b.legajo == ('LEG-'+ str(l)) and b.pin == p:
            menuBibliotecario(b,biblioteca)
            return
    print(
    f'---------- Datos Incorrectos, vuelva a intentarlo ----------\n')
    menuSesionBibliotecario()

def menuTipoPersona():
    print(
    f'---------- Selección de Logueo ----------\n'
    f'Por favor, seleccione su Rol:\n'
    f'1. Usuario.\n'
    f'2. Bibliotecario.\n'
    f'0. Salir.\n'
    f'----------------------------------------------')
    opcion=input('Ingrese opción deseada: ')
    if opcion == '1':
        menuSesionUsuario()
    elif opcion == '2':
        menuSesionBibliotecario()
    elif opcion == '0':
        menuPrincipal()

# ------------------------------ MENÚ PRINCIPAL ------------------------------
def menuPrincipal():
    print(
        f'-------------------- Menú --------------------\n'
        f'Bienvenido/a a la Biblioteca UNAB\n'
        f'Por favor Indique la opción que desea ejecutar:\n'
        f'1. Iniciar Sesión.\n'
        f'2. Registrarme.\n'
        f'0. Salir.\n'
        f'----------------------------------------------')
    opcion=input('Ingrese opción deseada: ')
    while True:
        if opcion == '1':
            menuTipoPersona()
            break
        elif opcion == '2':
            usuario=menuRegistroUsuario()
            menuUsuario(usuario, biblioteca)
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

