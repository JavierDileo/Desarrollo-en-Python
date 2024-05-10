# Dado un número entero positivo, mostrar su factorial. El factorial
# de un número se obtiene multiplicando todos los números enteros
# positivos que hay entre el 1 y ese número.

# Funcion para validar numeros positivos
def validarNumeroPositivo(numero):
    # Uso de un condicional para verificar que el numero ingresado sea positivo
    if numero < 0 :
        print("No es un numero positivo")
        numero = int (input("Ingrese un número entero positivo: "))
    return numero

# Inicializacion de la variable factorial en 1
factorial = 1

print("---------------CALCULAR EL FACTORIAL DE UN NUMERO---------------\n")
# Ingreso de Datos
numero = int(input("Ingrese un número entero positivo: "))
# llamado a la funcion validarNumeroPositivo para poder hacer la operación factorial
numero = validarNumeroPositivo(numero)
print("\n----------------------------------------------------------------")

# Operacion para calcular el factorial de un número ingresado
for i in range (numero):
    factorial *= ( numero - i )

# Impresion del resultado obtenido    
print("El Factorial de",numero,"es:", factorial,"\n")