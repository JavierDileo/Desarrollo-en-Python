# Escribir un programa que muestre la sumatoria de todos los
# múltiplos de 3 encontrados entre el 0 y el 100.

# Inicialización del acumulador en 0
suma = 0

print("-----Sumatoria de todos los múltipos de 3 entre el 0 y el 100.-----")
print("-------------------------------------------------------------------")

# Operación para sumar solo los numeros multiplos de 3 que hay del 0 al 100
for i in range(101):
    # Condicion para sumar solo los numeros multiplos de 3
    if  i %3 == 0:
        suma += i

# Impresion del resultado obtenido
print("\nLa suma de todos los múltiplos de 3 entre el 0 y el 100 es: ",suma)
print("\n-------------------------------------------------------------------")