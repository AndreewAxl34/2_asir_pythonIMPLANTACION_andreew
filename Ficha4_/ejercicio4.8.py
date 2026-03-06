#8.- Realizar la carga de valores enteros por teclado,
#almacenarlos en una lista. Finalizar la
#carga de enteros al ingresar el cero. Mostrar finalmente
#el tamaño de la lista.
lista=[]
cont=0
valor=int(input("Escribe un numero: "))
while valor != 0:
         lista.append(valor)
         cont+=1
         valor=int(input("Escribe un numero: "))
print(f"Los valores de la lista son: {lista}")
print(f"El tamaño de la fila es {len(lista)}")
