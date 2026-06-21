# Trabajo integrador final Grupo N°16  - Sistema de Gestión de Biblioteca Digital.

# -------------------- Importación de Clases, Funciones y Menú Principal --------------------
from clases import Biblioteca, Libro, Usuario, Bibliotecario
from funciones import mostrarInformacionGeneral
from menus import menuPrincipal

# -------------------- Instanciación de Biblioteca --------------------
biblioteca = Biblioteca()

# -------------------- Datos Iniciales --------------------
# 1. Creación y Alta de Libros 
# Formato: ('Titulo':String, 'Autor':String, 'Isbn':String, 'Año Publi':Number, 'Cant Pág':Number)
l1= Libro('El Alquimista', 'Paulo Coelho', '9788408130451', 1988, 192)
l2= Libro('Cien años de Soledad', 'Grabriel Garcia Márquez', '9788439733478', 1967, 496)
l3= Libro('1984', 'George Orwell', '9788466354141', 1949, 328)
l4= Libro('El Principito', 'Antoine de Saint-Exupéry', '9788498381498', 1943, 96)
l5= Libro('Harry Potter y la Piedra Filosofal', 'J.K. Rowling', '9788498389098', 1997, 288)
biblioteca.altaLibro(l1)
biblioteca.altaLibro(l2)
biblioteca.altaLibro(l3)
biblioteca.altaLibro(l4)
biblioteca.altaLibro(l5)

# 2. Creación, Alta y Listado de Usuarios
# Formato: ('Nombre':String, 'Apellido':String, 'DNI':Number, 'Email':String, 'Pin':Number)
u1= Usuario('Juan', 'Pérez', 12345678, 'juan@gmail.com', 1234)
u2= Usuario('María', 'Gómez', 11222333, 'maria@gmail.com', 4132)
biblioteca.altaUsuario(u1)
biblioteca.altaUsuario(u2)
biblioteca.listaUsuariosActuales()

# 3. Creación, Alta y Listado de Bibliotecarios
# Formato: ('Nombre':String, 'Apellido':String, 'LEG-000':String, 'Pin':Number)
b1= Bibliotecario('Susana', 'Gutierrez', 'LEG-821', 8567)
b2= Bibliotecario('Gerardo', 'Castro', 'LEG-301', 5678)
biblioteca.altaBibliotecario(b1)
biblioteca.altaBibliotecario(b2)
biblioteca.listaBibliotecariosActuales()

# 4. Creación, Alta y Listado de Prestamos
# Formato: ('Isbn del Libro':String, 'DNI del Usuario':Number)
biblioteca.registroDePrestamo('9788408130451', 11222333)
biblioteca.listarPrestamosActivos()

# -------------------- Mostrar Datos de forma Polimorfistica (Mostrar_info()) --------------------
objetos = [
    l1,                              # Libro 1
    b2,                              # Bibliotecario 2
    biblioteca.prestamos[0]          # Prestamo 
]
mostrarInformacionGeneral(objetos)

# -------------------- Ejecución del Menú Principal --------------------
menuPrincipal()