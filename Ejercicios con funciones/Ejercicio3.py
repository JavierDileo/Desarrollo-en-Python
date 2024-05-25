"""
Ejercicio Nro. 3
Solicitar números al usuario hasta que ingrese el cero. Por cada
uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la
sumatoria de todos los números ingresados y la suma de sus
dígitos. Reutilizar la misma función realizada en el ejercicio 2.

"""

bandera = True
listaDigitos = []   
listaNumeros = []

# Funcion para sumar los digitos de los numeros
def sumarDigitos(digitos):
    sumaDigitos = 0
    # Iteracion para hacer la operacion suma de digitos
    for i in digitos:
        sumaDigitos+= i
    return sumaDigitos

# Funcion para sumar los numeros ingresados
def sumarNumeros(listaNumeros):
    totalSuma = 0
    # Iteracion para hacer la operacion suma de numeros ingresados
    for i in listaNumeros:
        totalSuma += int(i)
    return totalSuma

# Funcion para generar lista con los digitos del numero
def generarListaDigitos(numeroIngresado):
    for numero in numeroIngresado :
        listaDigitos.append(int(numero))

while bandera:
    # Ingreso de datos
    numeroIngresado = input("ingrese un número o cero '0' para finalizar: ")
    
    # Condicion para salir del programa
    if numeroIngresado == '0':
        bandera = not bandera
        print("\nFinalizó el programa")
        
        # Impresion por pantalla y llamada ala funcion para sumar los numeros ingresados
        print(f"Sumatoria total de los números ingresados: {sumarNumeros(listaNumeros)}")
        
        # Llamada a la funcion para separar los digitos de la suma de los numeros ingresados
        generarListaDigitos(str(sumarNumeros(listaNumeros)))
        
        # impresion por pantalla y llamada ala funcion para sumar los digitos de la suma de los numeros
        print(f"La suma de los digitos es: {sumarDigitos(listaDigitos)} \n")
        continue
    else:
        # Se agrega el numero ingresado a una lista
        listaNumeros.append(numeroIngresado)
        
        # Llamada a la funcion para separar en digitos 
        generarListaDigitos(numeroIngresado)
        
        # impresion por pantalla y llamada a la funcion apra sumar los digitos
        print(f"La suma de los digitos es: {sumarDigitos(listaDigitos)}\n")
        listaDigitos = []