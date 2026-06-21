# Importación de la clase "Libro" del archivo Clases.py
from clases import Libro

# -------------------- Funciones de Usuarios --------------------
def usuarioHacerPrestamo(usuario, biblioteca):
    print(
        f'---------- Registrar Nuevo Prestamo ----------\n'
        f'Por favor, complete los siguientes campos:')
    d= int(input('DNI (Solo Números, sin Puntos ni Guiones Intermedios): '))
    i= input("Ingrese ISBN del libro: ")
    if usuario.dni == d:
        biblioteca.registroDePrestamo(
            i, usuario.dni)
    else:
        print('Los Datos son Incorrectos. Por favor, Intente Nuevamente.')
        usuarioHacerPrestamo()

def usuarioDevolucionPrestamo(usuario, biblioteca):
    print(
        f'---------- Devolución de un Prestamo ----------\n'
        f'Por favor, complete los siguientes campos:')
    d= int(input('DNI (Solo Números, sin Puntos ni Guiones Intermedios): '))
    i= input("Ingrese ISBN del libro: ")

    if usuario.dni == d:
        biblioteca.registrarDevolucion(i)
        print("Devolución registrada correctamente.")
    else:
        print('Los Datos son Incorrectos. Por favor, Intente Nuevamente')
        usuarioDevolucionPrestamo()

def usuarioModificarCuenta(usuario, biblioteca):
    print(
        f'---------- Modificar Cuenta ----------\n'
        f'Por favor, complete los siguientes campos - Deje vacío el dato que no quiera modificar:')
    d= int(input('DNI (Solo Números, sin Puntos ni Guiones Intermedios): '))
    nn= input('Ingrese el Nuevo Nombre: ')
    na= input('Ingrese el Nuevo Apellido: ')
    ne= input('Ingrese su Nuevo Email: ')
    np= int(input('Ingrese su Nuevo Pin (Solo Números): '))
    if usuario.dni == d:
        biblioteca.modificarUsuario(
            usuario.dni,
            nn if nn else None,
            na if na else None,
            ne if ne else None,
            np if np else None)
    else:
        print('Las Credenciales son Incorrectas. Por favor, Intente Nuevamente.')
        usuarioModificarCuenta(usuario, biblioteca)

# -------------------- Función de Bibliotecario --------------------
def bibliotecarioAltaLibro(bibliotecario, biblioteca):
    print(
        f'---------- Registrar un Libro Nuevo ----------\n'
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
        print('Los Datos son Incorrectos. Por favor, Intente Nuevamente.')
        bibliotecarioAltaLibro(bibliotecario, biblioteca)

def bibliotecarioModificarLibro(bibliotecario, biblioteca):
    print(
        f'---------- Modificar un Libro  ----------\n'
        f'Por favor, complete los siguientes campos - Deje en vacío los datos que no quiera modificar: ')
    l=int(input('Ingrese su N° de Legajo: '))
    if bibliotecario.legajo == 'LEG-'+str(l):
        i= input('Ingrese ISBN del libro: ')
        nt= input('Ingrese el Nuevo Título: ')
        na= input('Ingrese el Nuevo Autor: ')
        biblioteca.modificarLibro(
            i,
            nt if nt else None,
            na if na else None)
    else:
        print('Los Datos son Incorrectos. Por favor, Intente Nuevamente.')
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
        print('Los Datos son Incorrectos. Por favor, Intente Nuevamente.')
        bibliotecarioBajaLibro(bibliotecario, biblioteca)

def bibliotecarioBajaUsuarios(bibliotecario, biblioteca):
    print(
        f'---------- Dar de Baja Un Usuario ----------\n'
        f'Por favor, complete los siguientes campos:')
    l=int(input('Ingrese su N° de Legajo: '))
    if bibliotecario.legajo == 'LEG-'+str(l):
        d= int(input('DNI del Usuario (Solo Números, sin Puntos ni Guiones Intermedios):'))
        biblioteca.bajaUsuario(d)
    else:
        print('Los Datos son Incorrectos. Por favor, Intente Nuevamente.')
        bibliotecarioBajaUsuarios(bibliotecario, biblioteca)

# -------------------- Función Polimórfica --------------------
def mostrarInformacionGeneral(elementos):
    print("=== DEMOSTRACIÓN DE POLIMORFISMO ===")

    for elemento in elementos:
        print(elemento.mostrar_info())