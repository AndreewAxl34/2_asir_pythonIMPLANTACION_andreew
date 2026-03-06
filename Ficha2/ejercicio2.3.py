#3.- Desarrollar un programa que permita la carga de 10
#valores por teclado y nos muestre posteriormente la suma de
#los valores ingresados y su promedio.
#con while
cont=1
suma=0
while cont<=10:
     valor=int(input("ingresa valor "))
     suma=suma+valor
     cont+=1

print("La suma de los valores: "+str(suma))
print("El promedio es: "+str(suma/cont))
# otra forma
suma=0
for i in range(1,11):
     valor=int(input("ingresa valor "))
     suma=suma+valor
print("La suma de los valores: "+str(suma))
print("El promedio es: "+str(suma/cont))
