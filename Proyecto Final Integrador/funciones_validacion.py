
def validacion_nombre():
    # Bucle infinito para solicitar un nombre válido
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()  # Solicita el nombre y elimina espacios al inicio y final
        
        if not nombre:  # Verifica si el usuario no ingresó nada
            print("No ha ingresado un nombre, valor nulo no permitido.")  # Mensaje de error si el nombre está vacío
        else:
            if all(char.isalpha() or char.isspace() for char in nombre):  # Validad que se ingresen caracteres del alfabeto y espacios en el nombre
                return nombre  # Retorna el nombre válido
            else:
                print("Ingrese solo letras.")


def validacion_descripcion():
    # Permite ingresar una descripción, sin validación estricta
    while True:
        descripcion = input("Ingrese la descripcion del producto: ").strip()  # Solicita descripción y elimina espacios
        
        if not descripcion:  # Permite una descripción vacía pero avisa al usuario
            print("Nota: La descripción está vacía.")
        
        return descripcion  # Retorna la descripción ingresada


def validacion_categoria():
    # Bucle infinito para solicitar una categoría válida
    while True:
        categoria = input("Ingrese la categoria del producto: ").strip()  # Solicita la categoría y elimina espacios
        
        if not categoria:  # Verifica si el usuario no ingresó nada
            print("No ha ingresado una categoría, valor nulo no permitido.")  # Mensaje de error si está vacío
        else:
            return categoria  # Retorna la categoría válida


def validacion_cantidad():
    # Bucle infinito para solicitar una cantidad válida
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de unidades del producto: "))  # Solicita un valor entero
            
            if cantidad <= 0:  # Valida que la cantidad sea positiva
                print("La cantidad debe ser mayor a 0.")  # Mensaje de error si la cantidad es negativa o cero
            else:
                return cantidad  # Retorna la cantidad válida
        except ValueError as error:  # Maneja errores si el usuario ingresa un valor no entero
            print("Solo se admiten valores enteros.")  # Mensaje de error
            print(error)  # Muestra el detalle del error (opcional)


def validacion_precio():
    # Bucle infinito para solicitar un precio válido
    while True:
        try:
            precio = float(input("Ingrese el precio por unidad del producto: "))  # Solicita un valor decimal
            
            if precio <= 0:  # Valida que el precio sea positivo
                print("El precio debe ser mayor a 0.")  # Mensaje de error si el precio es negativo o cero
            else:
                return precio  # Retorna el precio válido
        except ValueError as error:  # Maneja errores si el usuario ingresa un valor no decimal
            print("Solo se admiten valores numéricos.")  # Mensaje de error
            print(error)  # Muestra el detalle del error (opcional)


def validacion_id():
    # Bucle infinito para solicitar un ID válido
    while True:
        try:
            id = int(input("Ingrese el ID: "))  # Solicita un valor entero para el ID
            
            if id <= 0:  # Valida que el ID sea positivo
                print("El ID debe ser un número mayor a 0.")  # Mensaje de error si el ID es negativo o cero
            else:
                return id  # Retorna el ID válido
        except ValueError as error:  # Maneja errores si el usuario ingresa un valor no entero
            print(f"Tipo de dato no válido, ingrese un número entero. {error}")  # Mensaje de error
