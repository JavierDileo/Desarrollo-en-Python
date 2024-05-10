# Requerir al usuario que ingrese un número entero positivo e
# imprimir todos los números correlativos entre el ingresado por el
# usuario y uno menos del doble del mismo.

# Funcion para validar numeros positivos
def validarNumeroPositivo(numero):
    # Uso de un condicional para verificar que el numero ingresado sea positivo
    if numero < 0 :
        print("No es un numero positivo")
        numero = int (input("Ingrese un numero entero positivo: "))
    return numero

print("----NUMEROS CORRELATIVOS HASTA UNO MENOS QUE EL DOBLE-----\n")
#Ingreso de datos
numero = int (input("Ingrese un numero entero positivo: "))

#Validacion mediante el uso de la funcion validarNumeroPositivo
numero = validarNumeroPositivo(numero)

# Asigno a la variable limite el valor del doble del numero ingresado. 
limite = (numero * 2)

print("\n-----------------NUMEROS DEL",numero,"AL",limite-1,"---------------------")
#Impresion por pantalla de los numeros 
for i in range (numero , limite):
    print(i,end=" - ")

print("\n----------------------------------------------------------")