# Solicitar al usuario que ingrese una frase y luego imprimir un
# listado de las vocales que aparecen en esa frase (sin repetirlas).

# Definicion de tupla de vocales
vocales = ('a','e','i','o','u')

print("----------¿Qué vocales contiene la frase?----------")

# Ingreso de Datos
frase = input("Ingrese una frase: ")

# Funcion para obtener las vocales que hay en la frase ingresada
def listadoDeVocales(frase, vocales):
    # Definicion de la lista de vocales que contiene la frase
    vocalesFrase = []
    for letra in frase:
        for vocal in vocales:
            #Comparacion de cada letra de la frase con cada una de las vocales de la tupla
            if letra == vocal:
                vocalesFrase.append(letra)
                # Si la letra se encuentra más de una vez en la lista, se elimina la repeticion.
                if vocalesFrase.count(letra) > 1:
                    vocalesFrase.remove(letra)
    # Se ordena la lista de vocales que hay en la frase
    vocalesFrase.sort()       
    
    # Impresion de Datos por pantalla
    print("----------------------------------------------------")        
    print("Frase:",frase)   
    print("\nLas vocales que contiene en la frase son:\n",vocalesFrase)
    print("----------------------------------------------------")  

# Llamada a la función
listadoDeVocales(frase, vocales)       