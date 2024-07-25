# Dado un diccionario con temperaturas en Celsius, convierte estas temperaturas a Fahrenheit. La fórmula para convertir Celsius a Fahrenheit es 
# 𝐹=𝐶×95+32F=C×59​+32.

celsius = {'Lunes': 20, 'Martes': 22, 'Miércoles': 19, 'Jueves': 21, 'Viernes': 18}


Fahrenheit = {dia: temp*9/5+32 for dia, temp in celsius.items()  }

print(Fahrenheit)