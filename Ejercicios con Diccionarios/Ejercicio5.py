# Escribir un programa que almacene el diccionario con los créditos
# de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4,
# 'Química': 5} y después muestre por pantalla los créditos de cada
# asignatura en el formato <asignatura> tiene <créditos> créditos,
# donde <asignatura> es cada una de las asignaturas del curso, y
# <créditos> son sus créditos. Al final debe mostrar también el
# número total de créditos del curso.

# Declaracion del diccionario de creditos de las asignaturas y declaracion del acumulador
creditosAsignaturas = {'Matemáticas': 6, 'Física': 4,'Química': 5}
creditosTotalDelCurso = 0

# Iteración sobre el diccionario creditosAsignaturas para mostrar por pantalla los creditos de cada asignatura
for asignaturas  in creditosAsignaturas:
    print(f"{asignaturas} tiene {creditosAsignaturas[asignaturas]} créditos")
    creditosTotalDelCurso += creditosAsignaturas[asignaturas]

# Mostrar por pantalla el total de los creditos del curso
print(f"\nNúmero total de créditos del curso: {creditosTotalDelCurso}")
