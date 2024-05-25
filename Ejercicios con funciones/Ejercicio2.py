"""
Ejercicio Nro. 2
Solicitar números al usuario hasta que ingrese el cero. Por cada
uno, mostrar la suma de sus dígitos (utilizando una función que
realice dicha suma).

"""

bandera = True
listaDigitos = []   

# Funcion para sumar los digitos de los numeros
def sumarDigitos(digitos):
    sumaDigitos = 0
    # iteracion para hacer la operación suma de digitos
    for i in digitos:
        sumaDigitos+= i
    return sumaDigitos

while bandera:
    # Ingreso de datos
    numeroIngresado = input("ingrese un número o cero '0' para finalizar: ")
    # Condicion para salir del programa
    if numeroIngresado == '0':
        bandera = not bandera
        print("\nFinalizó el programa")
        continue
    else:
        # Generar una lista separando los digitos
        for numero in numeroIngresado :
            listaDigitos.append(int(numero))
        print(f"La suma de los digitos es: {sumarDigitos(listaDigitos)}\n")
        
        # Volver la lista de los digitos a vacia
        listaDigitos = []