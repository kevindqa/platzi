print("acontinuacion me vas a dar do numeros para dividirlos y si el divisor es cero dara error")
num1 = int(input("num1 = "))
num2 =int (input("num2 = "))
if num2==0:
    print("error no se puede dividir")
else:
    print(num1/num2)
    print("si sepuede dividir")
if (num1%num2==0):
    print("no sobra na ")
else: print(f"sobro  {num1%num2}")