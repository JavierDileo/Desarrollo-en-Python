# Solicitar al usuario que ingrese una frase y luego imprimir la
# cantidad de vocales que se encuentran en dicha frase.

# Definicion de tupla de vocales
vocales = ('a','e','i','o','u')

print("----------¿Cuántas vocales tiene la frase?----------")

# Ingreso de Datos
frase = input("Ingrese una frase: ")

# Funcion para obtener las cantidad de vocales que hay en la frase ingresada
def cantidadVocales(frase, vocales):
    # Definicion de contador de vocales que tiene la frase
    contadorVocales = 0
    for letra in frase:
        for vocal in vocales:
            #Comparacion de cada letra de la frase con cada una de las vocales de la tupla
            if letra == vocal:
                # Se aumenta en 1 el contador si existe una vocal en la frase
                contadorVocales +=1      
    
    # Impresion de Datos por pantalla       
    print("\n----------------------------------------------------")        
    print("Frase: ",frase)   
    print("\nLa cantidad de vocales que aparecen en la frase son: ",contadorVocales)
    print("----------------------------------------------------")     
    
# Llamado a la función
cantidadVocales(frase, vocales)       