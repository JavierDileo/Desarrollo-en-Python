from funciones_dataBase import *  # Importa funciones relacionadas con la base de datos.
from funciones_validacion import *  # Importa funciones de validación de entradas.

# Menú principal que muestra las opciones disponibles para el usuario.
def menu_mostrarOpciones():
    print("-" * 30)
    print("""
        Menu de Opciones
        """)
    print("-" * 30)
    
    print("""
    1. Agregar Producto
    2. Mostrar Productos
    3. Actualizar
    4. Eliminar
    5. Buscar Producto
    6. Reporte Bajo Stock
    7. Salir
    """)
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para registrar un nuevo producto en la base de datos.
# 1. Captura los datos del producto.
# 2. Valida los datos mediante funciones externas.
# 3. Inserta el producto en la base de datos.
def menu_registrarProducto():
    print("")
    nombre = validacion_nombre()  # Valida el nombre del producto.
    descripcion = validacion_descripcion()  # Valida la descripción.
    categoria = validacion_categoria()  # Valida la categoría.
    cantidad = validacion_cantidad()  # Valida la cantidad (entero positivo).
    precio = validacion_precio()  # Valida el precio (número real positivo).
    
    producto = {
        "nombre" : nombre,
        "descripcion": descripcion,
        "categoria" : categoria,
        "cantidad": cantidad,
        "precio": precio
    }
    db_insertarProducto(producto)  # Inserta el producto en la base de datos.

# Función para mostrar todos los productos almacenados.
# 1. Recupera la lista de productos de la base de datos.
# 2. Itera y muestra cada producto si existen registros.
def menu_mostrarProductos():
    print("")
    lista_producto = db_getProductos()
    
    if lista_producto:
        for producto in lista_producto:
            print(f"ID: {producto[0]} -- Nombre: {producto[1]} -- Descripcion: {producto[2]} -- Categoria: {producto[3]} -- Cantidad: {producto[4]} -- Precio: {producto[5]}")  # Muestra cada producto.
    else:
        print("No hay productos cargados. Tabla vacía.")

# Función para actualizar la cantidad de un producto.
# 1. Solicita al usuario el ID del producto.
# 2. Busca el producto en la base de datos y verifica su existencia.
# 3. Solicita la nueva cantidad y la actualiza en la base de datos.
def menu_actualizarProducto():
    print("")
    print("Productos existentes en la base de datos:")
    menu_mostrarProductos()
    print("")
    print("Ingrese el 'ID' del producto a actualizar.")
    id = validacion_id()  # Valida el ID ingresado.
    producto = db_getProductoBy_id(id)  # Busca el producto.
    
    if not producto:
        print(f"No existe el producto con el ID: {id}")
    else:
        while True:
            try:
                nuevaCantidad = int(input(f"Cantidad actual {producto[4]} - Ingrese la nueva cantidad del producto: "))
                if not nuevaCantidad:
                    print("No ha ingresado una cantidad. Valor nulo no válido.")
                else:
                    break
            except ValueError as error:
                print(f"Valor no admitido. {error}")
    
        db_actualizarProducto(id, nuevaCantidad)  # Actualiza la cantidad.
        producto = db_getProductoBy_id(id)  # Verifica los cambios.
        print("Se actualizó correctamente.")
        print(f"ID: {producto[0]} -- Nombre: {producto[1]} -- Cantidad: {producto[4]}")

# Función para eliminar un producto.
# 1. Solicita el ID del producto.
# 2. Busca el producto y muestra su información.
# 3. Solicita confirmación y, si es afirmativa, elimina el producto.
def menu_eliminarProducto():
    print("")
    print("Productos existentes en la base de datos:")
    menu_mostrarProductos()
    print("")
    print("Ingrese el ID del producto a eliminar.")
    id = validacion_id()
    producto = db_getProductoBy_id(id)
    
    if not producto:
        print(f"No existe el producto con el ID: {id}")
    else:
        print("")
        print("Producto seleccionado para eliminar:")
        print(f"ID: {producto[0]} -- Nombre: {producto[1]} -- Descripcion: {producto[2]} -- Categoria: {producto[3]} -- Cantidad: {producto[4]} -- Precio: {producto[5]}")
        
        while True:
            print("")
            confirmacion = input(f"Desea eliminar el producto con el 'ID': {id} (S/N): ").capitalize()
            if confirmacion == 'S':
                db_eliminarProducto(id)  # Elimina el producto.
                print(f"Se ha eliminado el producto con el 'ID' {id}.")
                print("")
                print("Lista de productos existentes:")
                lista_productos = db_getProductos()  # Muestra los productos restantes.
                for producto in lista_productos:
                    print(f"ID: {producto[0]} -- Nombre: {producto[1]} -- Descripcion: {producto[2]} -- Categoria: {producto[3]} -- Cantidad: {producto[4]} -- Precio: {producto[5]}")
                break
            elif confirmacion == 'N':
                break

# Función para buscar un producto por su ID.
# 1. Solicita el ID del producto.
# 2. Recupera el producto de la base de datos.
# 3. Muestra la información del producto encontrado.
def menu_buscarProducto():
    print("")
    print("Ingrese el ID del producto que desea buscar.")
    id = validacion_id()
    producto = db_getProductoBy_id(id)
    
    if not producto:
        print(f"No existe un producto con el 'ID': {id}")
    else:
        print("")
        print("Producto encontrado:")
        print(f"ID: {producto[0]} -- Nombre: {producto[1]} -- Descripcion: {producto[2]} -- Categoria: {producto[3]} -- Cantidad: {producto[4]} -- Precio: {producto[5]}")

# Función para generar un reporte de productos con bajo stock.
# 1. Solicita al usuario el nivel mínimo de stock para el reporte.
# 2. Recupera los productos que cumplen con la condición.
# 3. Muestra la lista de productos con bajo stock.
def menu_reporteBajoStock():
    print("")
    try:
        minimoStock = int(input("Ingrese la cantidad mínima de stock para generar el reporte: "))
        if minimoStock <= 0:
            print("Valor no permitido, ingrese un entero positivo.")
        else:
            lista_bajoStock = db_getProductosBy_condition(minimoStock)
            if len(lista_bajoStock) == 0:
                print("No hay productos con bajo stock.")
            else:
                print("")
                print("Productos con bajo stock: ")
                for producto in lista_bajoStock:
                    print(f"ID: {producto[0]} -- Nombre: {producto[1]} -- Descripcion: {producto[2]} -- Categoria: {producto[3]} -- Cantidad: {producto[4]} -- Precio: {producto[5]}")
    except ValueError as error:
        print(f"Error en el tipo de dato, solo se permiten valores enteros. {error}")




