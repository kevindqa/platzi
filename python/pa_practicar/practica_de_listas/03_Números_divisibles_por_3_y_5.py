# Genera una lista con números del 1 al 100 que sean divisibles por 3 y 5.

numbers = [i for i in range(1,101) if i %3 ==0 and i %5 ==0]

print (numbers)