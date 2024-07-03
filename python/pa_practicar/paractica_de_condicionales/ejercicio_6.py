# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N 
# 
# el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

gender = input('Gender > ')  

Name = input('Name > ')

if    Name.lower() <'m' and gender == 'mujer':
    print (f'{Name} perteneces a el grupo A')
elif gender== 'hombre' and Name.lower <'n':
    print (f'{Name} perteneces a el grupo A')
else:
    print (f'{Name} perteneces a el grupo B')

