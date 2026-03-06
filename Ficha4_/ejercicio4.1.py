#1 .-Definir una lista que almacene 5 enteros.
#Sumar todos sus elementos y mostrar dicha suma.

#lista=[1,2,3,5]
#suma=sum(lista)
#print(f"La suma de la lista es {suma}")
#corregido

lista=[]
suma=0
for i in range(5):
        valor=int(input("introduce un numero: "))
        lista.append(valor)
        suma+=valor
print(f"El valor de la suma es {suma}")
