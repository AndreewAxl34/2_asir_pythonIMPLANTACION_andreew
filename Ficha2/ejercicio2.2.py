#2.- Codificar un programa que solicite la carga de un valor positivo
#y nos muestre desde 1 hasta el valor ingresado de uno en uno.
valor=int(input("introduce valor: "))
cont=1
while cont<=valor:
    print(cont)
    cont+=1
# otra forma
for i in range(1,valor+1):
    print(i)
