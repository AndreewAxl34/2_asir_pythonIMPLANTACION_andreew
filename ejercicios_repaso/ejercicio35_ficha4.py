# 35.- Solicitar por teclado dos enteros. El primer valor indica 
# la cantidad de elementos que
# crearemos en la lista. El segundo valor indica la cantidad de
#  elementos que tendrá cada
# una de las listas internas a la lista principal.
# Mostrar la lista y la suma de todos sus elementos.
entero1=int(input("El primer numero indicara la cantidad de numeros de la lista: "))
entero2=int(input("Cantidad de elementos cada lista: "))

lista=[]
for i in range(entero1):
       listaInterna=[]
       for j in range(entero2):
                valores=int(input("Escribe la cantidad de listas: "))
                listaInterna.append(valores)
       lista.append(listaInterna)

#for i in range(len(lista)):
#      suma=0
 #     suma+=lista[i]
# corregido la suma
suma_total=0
for i in range(len(lista)):
     for j in range(len(lista[i])):
            suma_total += lista[i][j]

print(f"la lista imprimida es: {lista}")
print(f"La suma de la lista es: {suma_total}")
 
