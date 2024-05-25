"""
Ejercicio Nro. 5
Escribir una función que, dado un número de DNI, retorne True si
el número es válido y False si no lo es. Para que un número de DNI
sea válido debe tener entre 7 y 8 dígitos.

"""
# Funcion para validar dni
def dniValido(numeroDni):
    # Condicion para validar dni
    if len(numeroDni) < 7 or len(numeroDni) > 8:
        dni = False
    else:
        dni = True
    return dni

print("----------------¿NÚMERO DE DNI VALIDO?---------------------")
# Ingrerso del dato
numeroDni = input("Ingrese el número de D.N.I.: ")
# Llamada a la funcion para validar dni
print(dniValido(numeroDni))