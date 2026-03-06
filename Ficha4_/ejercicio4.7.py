#7.- Definir una lista vacía y luego solicitar
#la carga de 5 enteros por teclado y añadirlos a
#la lista. Imprimir la lista generada.
lista=[]
cont=0
for i in range (5):
          valor=int(input("Introduce un valor: "))
          lista.append(valor)
          cont+=1
print(f"La lista es {lista}")
    
