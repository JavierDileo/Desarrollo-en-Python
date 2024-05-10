# Escribir un programa que pregunte al usuario su nombre, edad,
# dirección y teléfono y lo guarde en un diccionario. Después debe
# mostrar por pantalla el mensaje <nombre> tiene <edad> años,
# vive en <dirección> y su número de teléfono es <teléfono>.

# Declaracion y definicion del diccionario
persona = {"nombre" : "" , "edad" : "" , "direccion" : "" , "telefono" : ""}

# Bucle para cargar Datos en el diccionario
for campo in persona:
    entrada = input(f"Ingrese su {campo}: ")
    persona[campo] = entrada

# Impresion de la cadena con los datos ingresados
print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['direccion']} y su número de teléfono es {persona['telefono']}.")