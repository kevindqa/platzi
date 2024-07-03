# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta          	Tipo impositivo
# Menos de 10000€	       5%
# Entre 10000€ y 20000€	   15%
# Entre 20000€ y 35000€	   20%
# Entre 35000€ y 60000€	   30%
# Más de 60000€	45%
# # Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.}

Renta = int(input('Renta Anual >>> '))
if Renta < 10000:
    print('su tipo de renta es de 5%')
elif Renta < 20000:
    print('su tipo de renta es de 15%')
elif Renta <35000:
    print('su tipo de renta es de 20%')
elif Renta < 60000:
    print('su tipo de renta es de 30%')
elif Renta > 60000 :
    print('su tipo de renta es de 45%')


