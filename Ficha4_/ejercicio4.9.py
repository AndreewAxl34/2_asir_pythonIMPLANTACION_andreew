#9.- Almacenar en una lista los sueldos (valores float)
#de 5 operarios. Imprimir la lista y el
#promedio de sueldos.
lista=[]
cont=0
for i in range(5):
          sueldo=float(input("Escribe los sueldos: "))
          lista.append(sueldo)
          cont+=1
          for elemento in lista:
              cantidad=len(lista)
              suma=elemento+elemento
              promedio=suma/cantidad
print(f"La lista de los sueldos es: {lista}")
print(f"El promedio es: {promedio}")
