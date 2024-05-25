"""
Ejercicio Nro. 8
Escribir la función titulo(), la cual recibe un string y lo retorna
convirtiendo la primera letra de cada palabra a mayúscula y las
demás letras a minúscula, dejando inalterados los demás
caracteres. Precondición: el separador de palabras es el espacio: "
". Agregar doctests con suficientes casos de prueba para validar
que la función retorna el valor esperado ante distintos
argumentos.

"""

def titulo(cadena):
    """
    ejemplos:
    
    >>> titulo('HOLA COMO ESTAS')
    'Hola Como Estas'  
    
    >>> titulo("hOlA cOmO eStAs")
    'Hola Como Estas' 
    
    >>> titulo("hoLA coMO esTAs")
    'Hola Como Estas'  
    
    >>> titulo("holA comO estaS")
    'Hola Como Estas' 
    >>> titulo("HoLa CoMo EsTaS")
    'Hola Como Estas'  
    """
    
    nuevaCadena=""
    cadena =  cadena.split()
    
    palabras= [palabra.capitalize() for palabra in cadena]
    nuevaCadena = ' '.join(palabras)  
        
    return nuevaCadena

if __name__ == "__main__":
    import doctest
    doctest.testmod()