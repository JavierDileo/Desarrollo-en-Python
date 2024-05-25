"""
Ejercicio Nro. 4
Requerir al usuario que ingrese un número entero e informar si es
primo o no, utilizando una función booleana que lo decida.

"""

esPrimo = False

# Funcion booleana para validar un numero primo
def esPrimo(numero):
    contador = 0
    # iteracion para validar que solo se divida el numero por si mismo o por uno
    for i in range(1,numero+1):
        # Condicion para aumentar el contador si el resto de la division entre el numero y el iterador es cero
        if numero %i == 0:
            contador +=1
    # Condiciones para validar numeros primos
    # Si es igual a 1 o si no es entero, no es primo 
    if numero == 1 or numero < 0:
        esPrimo = False
        
    # si el contador es igual a 2, es primo    
    elif contador == 2:
        esPrimo = not False
    # Todos los demas casos, no son primos    
    else:
        esPrimo = False
    return esPrimo

print("----------------¿ES UN NÚMERO PRIMO?---------------------")
numero = int(input("Ingrese un número entero: "))
print(esPrimo( numero))
    