# Escribir un programa que pregunte una fecha en formato
# dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd
# de <mes> de aaaa donde <mes> es el nombre del mes.

# Declaracion de la tupla meses
meses = ("Enero" , "Febrero", "Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre",
        "Octubre","Noviembre","Diciembre")

# Declaracion del diccionario fecha
diccionarioFecha = {"dd" : 0, "mm" : 0 , "aaaa" : 0}


# Ingreso de la fecha con formato dd/mm/aaaa
fecha = input(f"Ingrese una fecha en el formato dd/mm/aaaa: ")

# Verificar que cumpla con el formato establecido
if '/' not in fecha or len(fecha) != 10:
    print("Formato de fecha invalido")
else:
    # Generar una lista con los datos de la fecha usando función split()    
    fecha = fecha.split("/")   
    
    # Verificar que se cumpla con las restricciones del calendario Gregoriano
    if int(fecha[0]) > 31 or int(fecha[0])< 1:
        print(f"No existe el dia {fecha[0]} en el calendario")
    elif int(fecha[1]) >12 or int(fecha[1]) <1 :
        print(f"No existe mes N° {fecha[1]} en el calendario ")
    elif len(fecha[2]) != 4 :
        print("Foramto  de año invalido")
    else:
        # Decalracion de la variable "i" para iterar en la lista ingreso
        i = 0
        
        # Iteración sobre el diccionario para agregarle las claves y sus repectivos valores
        for elemento in diccionarioFecha:
            diccionarioFecha[elemento] = fecha[i]
            i+=1      
        # Impresion por pantalla de la fecha según formato establecido en la consigna    
        print(f"{diccionarioFecha['dd']} de {meses[int(diccionarioFecha['mm'])-1]} de {diccionarioFecha['aaaa']}.")

