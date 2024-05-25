"""
Ejercicio Nro. 6
Escribir una función que, dado un string, retorne la longitud de la
última palabra. Se considera que las palabras están separadas por
uno o más espacios. También podría haber espacios al principio o
al final del string pasado por parámetro.

"""


# Funcion para obtener la longitud de la ultima palabra ingresada
def longitudUltimaPalabra(texto):
    
    # Convertir la cadena de texto en una lista con el metodo split()
    texto = texto.split()
    
    # utilización del indice -1 para identificar la ultima posición en la lista
    return f"La longitud de la palabra {texto[-1]} es: {len(texto[-1])}"

print("----------------LONGITUD DE LA ULTIMA PALABRA---------------------")
# Ingreso de la cadena de texto
texto = input("ingrese un texto: ")

# Impresión por pantalla de la longitud de la ultima palabra, haciendo llamada a la función longitudUltimaPalabra 
print(longitudUltimaPalabra(texto))    
