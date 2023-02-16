# programa para invertir numero de 4 digitos 

#input
n = int(input("digite el numero de 4 digitos para invertir: " ))

#processing
d1 = ((n%10)*1000)
pe = (n//10)
d2 = ((pe%10)*100)
pe = (pe//10)
d3 = ((pe%10)*10)
d4 = (pe//10)
ni = (d1+d2+d3+d4)

#output
print("el resultado de ni es: " +str(ni))
