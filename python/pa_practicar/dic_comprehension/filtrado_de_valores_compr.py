'''Ejercicio 4: Filtrado de valores
Instrucciones:
Dado un diccionario de estudiantes y sus notas, crea un nuevo diccionario que contenga solo a los estudiantes que hayan aprobado (nota mayor o igual a 60).
{clave: valor for elemento in iterable}
'''

notas = {'Ana': 78, 'Luis': 55, 'Carlos': 90, 'Maria': 40, 'Juan': 62}

aprobados = {name:   grade for  name, grade in notas.items() if grade>60  }



print(aprobados)