# -------------------- Importación de Clases y Funciones --------------------
from clases import Biblioteca, Usuario
from funciones import (
    usuarioHacerPrestamo, usuarioDevolucionPrestamo, usuarioModificarCuenta,
    bibliotecarioAltaLibro, bibliotecarioModificarLibro, bibliotecarioBajaLibro, bibliotecarioBajaUsuarios)

# -------------------- Intanciación de la clase Biblioteca --------------------
biblioteca=Biblioteca()

# -------------------- Menú de Usuario --------------------
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
                f'Opción NO válida.\n'
                f'Por favor Indique la opción que desea ejecutar:\n'
                f'1. Lista de Libros Actuales.\n'
                f'2. Prestamo de un Libro.\n'
                f'3. Devolución de un Libro.\n'
                f'4. Modificar un dato de mi cuenta.\n'
                f'0. Salir.\n'
                f'----------------------------------------------')
            opcion=input('Ingrese opción deseada: ')

# -------------------- Menú de Bibliotecarios --------------------
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
                f'Opción NO Válida\n'
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

# -------------------- Menú de Inicio de Sesión / Registro --------------------
def menuRegistroUsuario():
    print(
        f'---------- Registro de Usuario ----------\n'
        f'Por favor, complete los siguientes campos para crear una cuenta:')
    n=input('Nombre: ')
    a=input('Apellido: ')
    d=int(input('DNI (Solo Números, sin Puntos ni Guiones Intermedios): '))
    e=input('Email: ')
    p=int(input('Pin (Solo Números): '))
    nuevoUsuario= Usuario(nombre=n, apellido=a, dni=d, email=e, pin=p)
    biblioteca.altaUsuario(nuevoUsuario)
    return nuevoUsuario

def menuSesionUsuario():
    print(
    f'---------- Inicio de Sesión ----------\n'
    f'Por favor, Brinde estos datos:\n')
    d=int(input('Su DNI (Solo Números, sin Puntos ni Guiones Intermedios): '))
    p=int(input('Pin (Solo Números): '))
    for u in biblioteca.usuarios:
        if u.dni == d and u.pin == p:
            menuUsuario(u, biblioteca)
            return
    print(
    f'---------- Datos Incorrectos. Por favor, vuelva a intentarlo. ----------\n')
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
    f'---------- Datos Incorrectos. Por favor, vuelva a intentarlo. ----------\n')
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

# -------------------- Menú Principal --------------------
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

