# Escribir un programa que solicite al usuario una cantidad y luego
# itere la cantidad de veces dada. En cada iteración, solicitar al
# usuario que ingrese un número. Al finalizar, mostrar la suma de
# todos los números ingresados.

# Acumulador de los numeros ingresados
suma = 0

# Funcion para validar numeros positivos
def validarNumeroPositivo(numero):
    # Uso de un condicional para verificar que el numero ingresado sea positivo
    if numero < 0 :
        print("No es un numero positivo")
        numero = int (input("Ingrese un numero entero positivo: "))
    return numero
print("------SUMATORIA DE NUMEROS INGRESADOS------")

# Ingreso de la cantidad de iteraciones
cantidad = int (input("Ingresa la cantidad de veces a iterar: "))
#Validacion de numero positvo, no puede iterar con numeros negativos
cantidad = validarNumeroPositivo(cantidad)
print("\n------------INGRESO DE NUMEROS-------------")

# ingreso de Datos por cada iteracion
for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    # Suma de los numeros que van ingresando por vuelta
    suma += numero

print("\n---------------SUMATORIA--------------------")
#Impresion por pantalla del resultado de la sumatoria 
print("La suma de los números ingresados es: ",suma)    