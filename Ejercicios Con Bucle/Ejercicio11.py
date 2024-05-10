# Crear un algoritmo que muestre los primeros 10 números de la
# sucesión de Fibonacci. La sucesión comienza con los números 0 y
# 1 y, a partir de éstos, cada elemento es la suma de los dos números
# anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

# Inicializacion de la variable elemento en 0 y de la lista fibonacci con los dos primeros elementos 0 y 1
elemento = 0
fibonacci = [0,1]

# Operación para generar los 10 primeros números de la sucesión de Fibonacci
for i in range(1 ,9):
    # Operacion para generar el elemento de la sucesión
    elemento = fibonacci[i-1] + fibonacci[i]
    # Agregar el elemento a la lista fibonacci 
    fibonacci.append(elemento) 

print("------LOS PRIMEROS 10 NUMEROS DE LA SUCESION DE FIBONACCI------\n")
# Impresion de resultado obtenido
print(fibonacci)
print("---------------------------------------------------------------\n")