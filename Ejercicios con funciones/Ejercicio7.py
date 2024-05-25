"""
Ejercicio Nro. 7
Escribir un programa que permita al usuario obtener un
identificador para cada uno de los socios de un club. Para eso
ingresará nombre completo y número de DNI de cada socio,
indicando que finalizará el procesamiento mediante el ingreso de
un nombre vacío.
Precondición: el formato del nombre de los socios será: nombre
apellido. Podría ingresarse más de un nombre, en cuyo caso será:
nombre1 nombre2 apellido. Si un socio tuviera más de un apellido,
el usuario sólo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso
contrario, el programa debe dejar al usuario en un bucle hasta que
ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual
estará formado por: el primer nombre, la cantidad de letras del
apellido y los primeros 3 dígitos de su DNI. Ejemplo:
Nombre: Alba María Linares
DNI: 25834910
Alba7258.

"""
# Definicion de un diccionario, bandera y variable posicion
socios = {}
bandera = True
poscion = 0

# Funcion para validar numero de DNI
def dniValido(numeroDni):
    # Comparacion para validar DNI
    if len(numeroDni) < 7 or len(numeroDni) > 8:
        dni = False
    else:
        dni = True
    return dni

# Funcion para generar lista de digitos del numero ingresado
def generarListaDigitos(numeroIngresado):
    listaDigitos = []
    for numero in numeroIngresado :
        listaDigitos.append(numero)
    return listaDigitos

# Funcion para obtener la longitud del apeliido
def longitudApellido(texto):
    
    # Retorno de la cantidad de letras del apellido con el metodo len()
    return  len(texto)
    
# Bucle para el ingreso de Datos hasta que el usuario termine el programa
while bandera:
    # ingreso del nombre 
    nombre = input("Ingrese Nombre (Para finalizar, no ingrese el nombre): ")
    
    # condicion para terminar el programa si no ingresa un nombre
    if nombre == "":
        print("FInalizó el programa")
        bandera = False
        continue
    
    # Convertir cadena de texto en una lista con el metodo split()
    nombre = nombre.split()
    
    # Ingreso del Apellido
    apellido = input("Ingrese Apellido (si poseé dos apellidos sólo ingrese el primero): ")
    cantidadLetras = str(longitudApellido(apellido))
    # Ingreso del DNI
    dni = input("Ingrese el N° de D.N.I.: ")
    
    # Bucle donde en la condicion se llama a la funcion para validar DNI
    while dniValido(dni) == False:
        dni = input("Ingrese el N° de D.N.I.: ")
    
    # Declaracion de la variable primerosNumeros para guardar los 3 primero n° del dni
    primerosNumeros=""
    
    # Bucle para generar los primeros 3 digitos del dni
    for numero in range(3):
        # Variable donde se acumulan los 3 primeros numeros del dni, llamando a la funcion generarListaDigitos
        primerosNumeros += generarListaDigitos(dni)[numero] 
    
    # Se agregan al diccionario socios, las calves uniicas y los datos de los socios
    socios[nombre[0] + cantidadLetras + primerosNumeros]= []
    socios[nombre[0] + cantidadLetras + primerosNumeros].append(nombre)
    socios[nombre[0] + cantidadLetras + primerosNumeros].append(apellido)
    socios[nombre[0] + cantidadLetras + primerosNumeros].append(dni)
    
    # Impresion por pantalla de los datos y la clave unica
    # Condicion para imprimir uno o dos nombres segun tuviere el usuario
    if len (nombre) == 2:
        print(f"Nombre: {nombre[0]} {nombre[1]} {apellido}")
    else:
        print(f"Nombre: {nombre[0]} {apellido}")
        
    print(f"DNI: {dni}")
    
    # Se genera con la funcion list() una lista de las claves del diccionario y se devuelve la clave en la posicion especifica
    print(f"Clave unica: {list(socios.keys())[poscion]}")
    
    # Se aumenta en una unidad la posicion
    poscion +=1
