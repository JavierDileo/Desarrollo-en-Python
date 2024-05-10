# Escribir un programa que guarde en una variable el diccionario
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa
# y muestre su símbolo o un mensaje de aviso si la divisa no está en
# el diccionario.

# Declaracion y definicion del diccionario
diccionarioDivisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

# Ingreso del Dato
divisa = input("¿Qué divisia desea seleccionar? ")

#Formatear la cadena con la primer letra en mayúscula y las siguientes en minúsculas.
divisa = divisa.capitalize()

# Verificar que la divisa este en el diccionario
if divisa in diccionarioDivisas:
    # Guardar en la variable mensaje una cadena con el simbolo de la divisa 
    mensaje= f"El simbolo de la divisa {divisa} es: {diccionarioDivisas[divisa]}"
else:
    # Guardar en la variable mensaje una cadena para avisar que no se encuentra la divisa en el diccionario
    mensaje = "La divisa no se encuentra en el diccionario"

# Imprimir la variable mensaje
print(mensaje)