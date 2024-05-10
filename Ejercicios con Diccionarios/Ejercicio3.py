# Escribir un programa que guarde en un diccionario los precios de
# las frutas de la tabla, pregunte al usuario por una fruta, un número
# de kilos y muestre por pantalla el precio de ese número de kilos
# de fruta. Si la fruta no está en el diccionario debe mostrar un
# mensaje informando de ello.

# Declaracion del diccionario de precios de las frutas
preciosFrutas = {"Platano" : 1.35 , "Manzana" : 0.80 , "Pera" : 0.85 , "Naranja" : 0.70}

# Carga de Datos
fruta = input("¿Qué fruta desea comprar?: ")

# Formatear la cadena con la primer letra en mayúscula y las siguientes en minúsculas.
fruta = fruta.capitalize()

# operacion de precio por kilo de la fruta seleccionada e impresion por pantalla
resultado = 0
# Verificar que exista en el diccionario la fruta seleccionada
if fruta in preciosFrutas :
    # Ingreso del Dato
    kilos = float(input("¿Cuántos kilos desea comprar?: "))
    resultado = kilos*preciosFrutas[fruta]
    print(f"El precio de {fruta} por la cantidad de {kilos} Kg es: {resultado} pesos")
else:
    print(f"La fruta {fruta} no se encuentra en el diccionario")