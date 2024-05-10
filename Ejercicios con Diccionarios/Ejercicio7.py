# Escribir un programa que cree un diccionario simulando una cesta
# de la compra. El programa debe preguntar el artículo y su precio y
# añadir el par al diccionario, hasta que el usuario decida terminar.
# Después se debe mostrar por pantalla la lista de la compra y el
# coste total, con el siguiente formato.

# Declaracion del diccionario, bandera y acumulador
listaCompras ={}
bandera = True
total = 0

# Bucle para agregar articulos y precios a la lista de compras
while bandera:
    # Ingreso de Datos
    clave = input("Articulo que desea agregar a la lista de compras: ")
    valor = int(input("Ingrese el precio del articulo: "))

    # Agregar clave y valor al diccionario
    listaCompras[clave] = valor

    # Decisión para continuar agregando datos a la lista de compras
    seguir = input("¿Desea seguir cargando articulos a la lista de compras? (Si / No): ")
    # poner toda la cadena en minuscula
    seguir = seguir.lower()
    # Si no continua bandera es False
    if seguir == 'no' :
        bandera = False

# Impresion por pantalla de la lista de compras y el total a pagar
print("\nLISTA DE LA COMPRA")
print("---------------------------------------")
print("Articulo                        Precio")
print("---------------------------------------")
for articulo in listaCompras:
    # impresion por pantalla de cada articulo con su precio
    print(articulo , "                          ","$",listaCompras[articulo])
    
    # Suma total de la compra
    total += listaCompras[articulo]
            
print("---------------------------------------")
print("TOTAL                         ","$",total)