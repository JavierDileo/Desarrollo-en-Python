# Importar el módulo sqlite3 para interactuar con bases de datos SQLite
import sqlite3

# Ruta de la base de datos SQLite
ruta = r"C:\Users\Estudiante\Documents\python tech\inventario.db"

# Función para crear la tabla 'productos' si no existe
def crearTablaProductos():
    try:
        # Conexión a la base de datos
        connection = sqlite3.connect(ruta)
        cursor = connection.cursor()
        
        # Crear la tabla 'productos' con las columnas especificadas
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Clave primaria autoincremental
                nombre TEXT NOT NULL,                  -- Nombre del producto, obligatorio
                descripcion TEXT,                     -- Descripción del producto, opcional
                categoria TEXT NOT NULL,              -- Categoría del producto, obligatorio
                cantidad INTEGER NOT NULL,            -- Cantidad disponible, obligatorio
                precio REAL NOT NULL                  -- Precio del producto, obligatorio
            )"""
        )
        # Guardar los cambios en la base de datos
        connection.commit()
    except sqlite3.Error as erorr:
        # Capturar e informar si ocurre un error al crear la tabla
        print("Hubo un error al crear la tabla, algo falló")
    finally:
        # Cerrar la conexión con la base de datos
        connection.close()

# Función para insertar un nuevo producto en la tabla 'productos'
def db_insertarProducto(producto):
    # Conexión a la base de datos
    connection = sqlite3.connect(ruta)
    cursor = connection.cursor()
    
    # Consulta SQL para insertar un producto
    query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?,?,?,?,?)"
    placeholders = (
        producto["nombre"],       # Nombre del producto
        producto["descripcion"],  # Descripción del producto
        producto["categoria"],    # Categoría del producto
        producto["cantidad"],     # Cantidad disponible
        producto["precio"]        # Precio del producto
    )
    # Ejecutar la consulta con los datos proporcionados
    cursor.execute(query, placeholders)
    connection.commit()  # Guardar los cambios
    connection.close()   # Cerrar la conexión

# Función para obtener todos los productos de la tabla 'productos'
def db_getProductos():
    connection = sqlite3.connect(ruta)
    cursor = connection.cursor()
    
    # Consulta SQL para seleccionar todos los registros de la tabla
    query = "SELECT * FROM productos"
    cursor.execute(query)
    
    # Obtener todos los productos como una lista de tuplas
    lista_prodcutos = cursor.fetchall()
    connection.close()  # Cerrar la conexión
    return lista_prodcutos

# Función para obtener un producto específico por su ID
def db_getProductoBy_id(id):
    connection = sqlite3.connect(ruta)
    cursor = connection.cursor()
    
    # Consulta SQL para seleccionar un producto por ID
    query = "SELECT * FROM productos WHERE id = ?"
    placeholders = (id,)  # Parámetro de la consulta
    
    cursor.execute(query, placeholders)
    producto = cursor.fetchone()  # Obtener el primer resultado
    connection.close()  # Cerrar la conexión
    return producto

# Función para actualizar la cantidad de un producto por su ID
def db_actualizarProducto(id, nuveaCantidad):
    connection = sqlite3.connect(ruta)
    cursor = connection.cursor()
    
    # Consulta SQL para actualizar la cantidad de un producto
    query = ("UPDATE productos SET cantidad = ? WHERE id = ?")    
    placeholders = (nuveaCantidad, id)  # Parámetros de la consulta
    
    cursor.execute(query, placeholders)
    connection.commit()  # Guardar los cambios
    connection.close()   # Cerrar la conexión

# Función para eliminar un producto por su ID
def db_eliminarProducto(id):
    connection = sqlite3.connect(ruta)
    cursor = connection.cursor()
    
    # Consulta SQL para eliminar un producto por ID
    query = "DELETE FROM productos WHERE id = ?"
    placeholders = (id,)  # Parámetro de la consulta
    
    cursor.execute(query, placeholders)
    connection.commit()  # Guardar los cambios
    connection.close()   # Cerrar la conexión

# Función para obtener productos con una cantidad menor a un valor específico
def db_getProductosBy_condition(minimo_stock):
    connection = sqlite3.connect(ruta)
    cursor = connection.cursor()
    
    # Consulta SQL para seleccionar productos con cantidad menor a un valor dado
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholders = (minimo_stock,)  # Parámetro de la consulta
    
    cursor.execute(query, placeholders)
    listaProdcutos = cursor.fetchall()  # Obtener los resultados
    connection.close()  # Cerrar la conexión
    return listaProdcutos
