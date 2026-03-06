#5.- Definir una lista por asignación con 5 enteros.
#Mostrar por pantalla solo los elementos con valor
#iguales o superiores a 7.
lista=[]
cont=0
for i in range(5):
           valor=int(input("escribimos el valor"))
           lista.append(valor)
for elemento in lista:
           if (elemento >= 7):
             print(elemento)
for i in range(len(lista)):
        if (lista[i]>=7):
              print(lista[i])
