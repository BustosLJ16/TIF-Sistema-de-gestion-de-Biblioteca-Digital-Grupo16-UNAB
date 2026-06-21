# -------------------- Importación de Clases y Funciones --------------------
from clases import Biblioteca, Libro, Usuario, Bibliotecario

# -------------------- Encabezados y Subtitulos --------------------
def encabezado(titulo):
    print("\n" + "=" * 60)
    print(titulo.center(60))
    print("=" * 60)

def subtitulo(titulo):
    print("\n" + "-" * 60)
    print(titulo)
    print("-" * 60)

biblioteca= Biblioteca()

# -------------------- Función de Prueba de Libros --------------------
def pruebaLibros(biblioteca):
    encabezado("PRUEBAS DE LIBROS")
    subtitulo("Alta de Libros")
    # Creación de Libros | Titulo, Autor, ISBN, Año Publicación, Cantidad de Páginas
    l1= Libro('El Alquimista', 'Paulo Coelho', '9788408130451', 1988, 192)
    l2= Libro('Cien años de Soledad', 'Grabriel Garcia Márquez', '9788439733478', 1967, 496)
    l3= Libro('1984', 'George Orwell', '9788466354141', 1949, 328)

    # Alta de Libros
    biblioteca.altaLibro(l1)
    biblioteca.altaLibro(l2)
    biblioteca.altaLibro(l3)

    # Listado Actual
    subtitulo("Listado de Libros")
    biblioteca.listaLibrosActuales()

    # Modificar Libro | Formato: ISBN, Dato a cambiar (tituloNuevo, autorNuevo)
    subtitulo("Modificación de Libros")
    biblioteca.modificarLibro("9788466354141", tituloNuevo="Harry Potter 2") 
    biblioteca.listaLibrosActualizados()

    # Baja de Libro | Formato: ISBN
    subtitulo("Baja de Libros")
    biblioteca.bajaLibro("9788439733478")
    biblioteca.listaLibrosActualizados()
pruebaLibros(biblioteca)

def pruebaUsuarios(biblioteca):
    encabezado("PRUEBAS DE USUARIOS")
    subtitulo("Alta de Usuarios")

    # Creación de Usuario | Formato: Nombre, Apellido, Dni, Email, Pin
    u1= Usuario('Juan', 'Perez', '12345678', 'juan@mail.com', 1234)
    u2= Usuario('Maria', 'Gomez', '11222333', 'maria@mail.com', 5231)
    u3= Usuario('Sabrina', 'Jimenez', '98765432', 'Sabrina@mail.com', 4321)

    # Alta de Usuarios
    biblioteca.altaUsuario(u1)
    biblioteca.altaUsuario(u2)
    biblioteca.altaUsuario(u3)

    # Listado de Usuarios
    subtitulo("Listado Actual de Usuarios")
    biblioteca.listaUsuariosActuales()

    # Modificar Usuario | Formato: Dni, Dato a cambiar (nuevoNombre, nuevoApellido, nuevoEmail,nuevoPin)
    subtitulo("Modificación de Usuarios")
    biblioteca.modificarUsuario("11222333", nuevoEmail='Mariagomez@gmail.com')
    biblioteca.listaUsuariosActualizados()

    # Baja de Usuario | Formato: Dni
    subtitulo("Baja de Usuario")
    biblioteca.bajaUsuario("98765432")
    biblioteca.listaUsuariosActualizados()
pruebaUsuarios(biblioteca)

def pruebaBibliotecarios(biblioteca):
    encabezado("PRUEBAS DE BIBLIOTECARIOS")
    subtitulo("Alta de Bibliotecarios")

    # Creación de Bibliotecarios | Formato: Nombre, Apellido, Legajo(LEG-000), Pin
    b1=Bibliotecario('Susana', 'Gutierrez', 'LEG-821', 1234)
    b2=Bibliotecario('Pedro', 'Martinez', 'LEG-301', 5678)
    b3=Bibliotecario('Raul', 'Alvarez', 'LEG-980', 4321)

    # Alta de Bibliotecarios
    biblioteca.altaBibliotecario(b1)
    biblioteca.altaBibliotecario(b2)
    biblioteca.altaBibliotecario(b3)

    # Lista de Bibliotecarios
    subtitulo("Listado de Bibliotecarios")
    biblioteca.listaBibliotecariosActuales()

    # Baja de Bibliotecarios | Formato: N° Legajo EJ:000
    subtitulo("Baja de Bibliotecarios")
    biblioteca.bajaBibliotecario(301)
    biblioteca.listaBibliotecariosActuales()
pruebaBibliotecarios(biblioteca)

def pruebaPrestamos(biblioteca):
    encabezado("PRUEBAS DE Prestamos")
    subtitulo("Registro de Prestamo")

    # Registrar Prestamo | Formato: ISBN, DNI Usuario
    biblioteca.registroDePrestamo('9788408130451', "11222333")
    biblioteca.registroDePrestamo('9788466354141', "12345678")

    # Lista de Prestamos activos
    subtitulo("Lista de Prestamos Activos")
    biblioteca.listarPrestamosActivos()

    # Registrar Prestamo de libro ya reservado | Formato: ISBN, DNI Usuario
    subtitulo("Registrar Prestamo de libro ya reservado")
    biblioteca.registroDePrestamo("9788408130451", "12345678")
    biblioteca.listarPrestamosActivos()

    # Registrar Devolución | Formato: ISBN,
    subtitulo("Registrar Devolucion de libro reservado")
    biblioteca.registrarDevolucion("9788408130451")

    # Registrar Devolución de un libro Ya devuelto | Formato: ISBN,
    subtitulo("Registrar Devolucion Nuevamente de un mismo libro reservado")
    biblioteca.registrarDevolucion("9788408130451")

    # Registrar Devolución de un Libro inexistente
    subtitulo("Devolución de un libro Inexistente")
    biblioteca.registroDePrestamo("999","12345678")

    # Registrar Devolución de un usuario inexistente
    subtitulo("Devolución con Usuario Inexistente")
    biblioteca.registroDePrestamo("9788408130451","99999999")  
pruebaPrestamos(biblioteca)

def pruebaSingleton():
    encabezado("PRUEBA DE SINGLETON")
    subtitulo("Creación de Instancias")

    b1 = Biblioteca()
    b2 = Biblioteca()

    print(f"¿b1 y b2 son la misma instancia?: {b1 is b2}")

    subtitulo("Modificación desde una Instancia")
    libroPrueba = Libro(
        "Libro Singleton","Autor Demo", "999", 2026, 100)
    b1.libros.append(libroPrueba)

    subtitulo("Verificación desde la Segunda Instancia")
    for libro in b2.libros:
        print(libro.mostrar_info())
pruebaSingleton()