# Escribir un programa que muestre la sumatoria de todos los
# números entre el 0 y el 100.

# inicializacion del acumulador en 0
suma = 0

print("------Sumatoria de de todos los números entre el 0 y el 100.-------")
print("-------------------------------------------------------------------")

# Realizacion de la suma de los primero 100 numeros
for i in range(101):
    suma += i

# Impresion por pantalla del resultado obtenido
print("\nLa suma de todos los números entre el 0 y el 100 es: ",suma)
print("\n-------------------------------------------------------------------")