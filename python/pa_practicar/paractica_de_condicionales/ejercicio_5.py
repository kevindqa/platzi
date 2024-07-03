# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.


age= (int (input('Edad > ')))


monthly_earn=(int (input('month_earn > 45')))

if age > 16 and monthly_earn >=  1000:
    print ('tiene que triutar')
else:
    print ('no tiene que tributar')    