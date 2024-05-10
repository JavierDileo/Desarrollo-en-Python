# Escribir un programa que cree un diccionario vacío y lo vaya
# llenado con información sobre una persona (por ejemplo nombre,
# edad, sexo, teléfono, correo electrónico, etc.) que se le pida al
# usuario. Cada vez que se añada un nuevo dato debe imprimirse el
# contenido del diccionario.

# Declaracion del diccionario persona y declaracion de una bandera
persona = {}
bandera = True

# Bucle para agregar claves y valores al diccionario hasta que el usuario decida
while bandera:
    # Ingreso de Datos
    clave = input("Ingrese el nombre del campo: ")
    valor = input("Ingrese el valor del campo: ")
    
    # Agregar clave y valor al diccionario persona
    persona[clave] = valor
    
    # Mostrar por pantalla el contenido del diccionario persona
    print(f"\nContenido del diccionario\n {persona}\n")
    
    # Decisión para continuar agregando datos al diccionario
    seguir = input("¿Desea seguir? (Si / No): ")
    
    # Poner toda la cadena en minusculas
    seguir = seguir.lower()
    
    # Si no desea continuar bandera es False
    if seguir == 'no' :
        bandera = False        
