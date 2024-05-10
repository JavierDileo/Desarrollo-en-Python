# Escribir un programa que permita al usuario ingresar 6 números
# enteros, que pueden ser positivos o negativos. Al finalizar, mostrar
# la sumatoria de los números negativos y el promedio de los
# positivos.
# No olvides que no es posible dividir por cero, por lo que es
# necesario evitar que el programa arroje un error si no se
# ingresaron números positivos.

# Definicion de las listas para guardar los numeros positivos y negativos respectivamente
numPositivos = []
numNegativos = []

# Funcion para calcular el promedio de los valores de una lista
def calcularPromedio(listaNumeros):
    suma = 0
    # Condicional para saber si la lista existe, no esta vacia.
    if listaNumeros:
        # Operacion para generar el promedio de los valores de la lista
        for numero in listaNumeros:
            suma += numero
            promedio = suma / len(listaNumeros)
        return promedio    
    else:
        # Si la lista esta vacia
       return  print("Lista de números vacia, no se puede dividir por 0")
   

# Funcion para calcular la suma de todos los valores de una lista
def sumatoriaDenumeros (listaNumeros):
    suma = 0
    # Operacion para generar la sumatoria de todos los valos de la lista
    for numero in listaNumeros:
        suma += numero
    return suma

print("------INGRESE 6 NUMEROS ENTEROS POSITIVOS O NEGATIVOS------\n")

# Ingreso de Datos
for i in range (1,7):
   print("Ingrese el",i,"° número:")
   numero = int(input())
   #Condiciones para diferenciar numeros positivos y negativos y, agregarlos a sus respectivas listas
   if numero >= 0:
       numPositivos.append(numero)
   elif numero < 0:
       numNegativos.append(numero)


# Impresion de los resultados obtenidos
print("\n---------------NUMEROS POSITIVOS INGRESADOS---------------")
print(numPositivos)
print("\n---------------NUMEROS NEGATIVOS INGRESADOS---------------")
print(numNegativos)       

print("\n-----------------------------------------------------------")

print("------------------------PROMEDIO---------------------------")
print("El Promedio de los números positivos es:",calcularPromedio(numPositivos))
print("-----------------------------------------------------------\n")

print("------------------------SUMATORIA--------------------------")
print("La sumatoria de los números negativos es:",sumatoriaDenumeros(numNegativos))
print("-----------------------------------------------------------\n")
