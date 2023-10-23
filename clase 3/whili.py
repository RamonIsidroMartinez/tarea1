numero =1
sueldo =0
total =0

while numero <=5:
    sueldo = int(input("entre sueldo:"))
    total = total + sueldo
    numero = numero + 1
    
    print ("total de sueldos :",total)