# <<<<<<<   while es un ciclo  >>>>>>
''''
counter=0
while counter < 10:
    counter += 1
    print(counter)


counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break            # break interrumpe de manera forzada un ciclo
    print (counter)   

'''

counter = 0

while counter < 20:
    counter +=1 
    if counter < 15:
        continue
    print(counter)