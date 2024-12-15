from funciones_menu import *  # Importa todas las funciones definidas en el módulo `funciones_menu`
from funciones_dataBase import crearTablaProductos  # Importa la función para crear la tabla de productos en la base de datos

def main():  # Define la función principal del programa
    
    # Llama a la función que asegura que la tabla de productos exista en la base de datos antes de realizar cualquier operación.
    crearTablaProductos()  

    while True:  # Bucle infinito para mantener el programa corriendo hasta que el usuario decida salir.
        
        # Llama a la función que muestra el menú y captura la opción seleccionada por el usuario.
        opcion = menu_mostrarOpciones()  
        
        print("ha seleccionado: ", opcion)  # Muestra en la consola la opción seleccionada por el usuario.

        # Si la opción es 1, llama a la función para registrar un nuevo producto.
        if opcion == "1":
            menu_registrarProducto()  
        
        # Si la opción es 2, llama a la función para mostrar todos los productos registrados.
        elif opcion == "2":
            menu_mostrarProductos()  
        
        # Si la opción es 3, llama a la función para actualizar los datos de un producto existente.
        elif opcion == "3":
            menu_actualizarProducto()  
        
        # Si la opción es 4, llama a la función para eliminar un producto por su ID.
        elif opcion == "4":
            menu_eliminarProducto()  
        
        # Si la opción es 5, llama a la función para buscar un producto específico por su ID.
        elif opcion == "5":
            menu_buscarProducto()  
        
        # Si la opción es 6, llama a la función para generar un reporte de productos con bajo stock.
        elif opcion == "6":
            menu_reporteBajoStock()  
        
        # Si la opción es 7, agradece al usuario y finaliza el programa.
        elif opcion == "7":
            print("Gracias por usar nuestra App")  
            break  # Rompe el bucle infinito, terminando el programa.
        else:
            print("Opción no válida. Por favor, elija una opción válida.")  # Mensaje de error en caso de que la opción ingresada no sea válida.

        # Pregunta al usuario si desea continuar o salir del programa. Convierte la respuesta a mayúscula inicial para consistencia.
        continuar = input("\nIngrese 'S' para salir o cualquier tecla para continuar: ").capitalize()  

        if continuar == "S":  # Si el usuario ingresa 'S', finaliza el programa.
            print("\nGracias por usar nuestra App")  # Agradece al usuario por usar la aplicación.
            break  # Rompe el bucle infinito, terminando el programa.

main()  # Llama a la función principal para iniciar el programa.
