#36.- Definir dos listas de 3 elementos.
#La primer lista cada elemento es una sublista con el nombre del padre y la madre de una
#familia.
#La segunda lista está constituida por listas con los nombres de los hijos de cada familia.
#Puede haber familias sin hijos.
#Imprimir los nombres del padre, la madre y sus hijos.
#También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.
#lista1=[]
#for i in range(3):
#       sublista1=[]
#       for i in range(1):
#           padre=input("Escribe el nombre del padre: ")
#           madre=input("Escribe el nombre del madre: ")
#           sublista1.append(padre,madre)
 #      lista1.append(sublista1)

#lista2=[]
#for i in range(3):
#       sublista2=[]
#       for i in range(1):
#           hijo=input("Escribe el nombre del hijo: ")
#           hija=input("Escribe el nombre del hija: ")
 #          sublista2.append(hijo,hija)
#       lista2.append(sublista2)

#print(f"Los padres de cada familia son: lista1")
#print(f"Los padres de cada familia son: lista2")
# corregido
lista1=[] #Padres
lista2=[] #Hijos

for i in range(3):
        padre=input("Escribe el nombre del padre: ")
        madre=input("Escribe el nombre del madre: ")
        lista1.append([padre,madre])
        #Crearemos una nueva lista para ver la cantidad de hijos
        cantidad_hijos=int(input("Escribe la cantidad de hijos"))
        hijos_familia=[]
        for j in range(cantidad_hijos):
           nombre=input("Escribe el nombre del hijo: ")
           hijos_familia.append(nombre)
        lista2.append(hijos_familia)

for i in range(3):
      padre=lista1[i][0]
      madre=lista1[i][1]
      hijos=lista2[i]

      print(f"Padres: {padre} y {madre}. Hijos: {hijos}")

for i in range(3):
      padre = lista1[i][0]
      cantidad = len(lista2[i])
      print(f"Padre: {padre} - cantidad de hijos: {cantidad} ")


