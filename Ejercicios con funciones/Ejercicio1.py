"""
Ejercicio Nro. 1
Solicitar al usuario que ingrese su dirección email. Imprimir un
mensaje indicando si la dirección es válida o no, valiéndose de una
función para decidirlo. Una dirección se considerará válida si
contiene el símbolo "@".

"""
# Ingreso de e-mail
direccionMail = input("Ingrese su dirección de e-mail: ")

# Funcion para validar e-mail
def esMail (direccion):
    # Dividir en partes la direccion ingresada cada vez que el programa lea el caracter '@'
    partes = direccion.split('@')
    
    # Condicion para validar el e-mail
    if len(partes) == 2 and '.' in partes[1]:
        print(f"\n{direccion}")
        print("Es una direccion de email válida")
    else:
        print(f"\n{direccion}")
        print("No es una dirrección de email válida")

# Lalamada a la funcion esMail        
esMail(direccionMail)