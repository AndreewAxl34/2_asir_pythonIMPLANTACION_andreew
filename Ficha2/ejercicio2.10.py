#10.-Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cual de las dos listas tiene un valor
#acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")

#lista1: int(input("Esta es la lista1: "))
#lista2: int(input("Esta es la lista2: "))
#for i in range (1,16):
 #       if(lista1 > 15):
 #           print("Lista 1 es mayor")
 #       elif(lista2 > 15):
#            print("lista 2 es mayor")
#        elif(lista1 == lista2):
 #            print("Las listas son iguales")
 #       else:
 #         print("error")
#print("adios")
# corregido
suma1=0
suma2=0
for i in range (1,16):
    valor=int(input("Introduce el valor de lista1: "))
    suma1=suma1+valor

for i in range (1,16):
    valor=int(input("Introduce el valor de lista2: "))
    suma2=suma2+valor    

if suma1>suma2:
    print(f"La suma de lista1 {suma1} es mayor que lista2 {suma2}")
elif suma2 > suma1:
    print(f"La suma de lista 2 {suma2} es mayor que lista1 {suma1} ")
else:
    print("Las sumas son iguales")
print("adios")
