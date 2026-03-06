#21.- Definir una lista de enteros por asignación en el 
#bloque principal. Llamar a una función que reciba la lista 
#y nos retorne el producto de todos sus elementos. 
#Mostrar dicho producto en el bloque principal de nuestro programa. 
#def crearlista():
  #  lista=[]
##    for i in range(6):
#        numero=int(input("Escribe el valor: "))
#        lista.append
#    return lista

#def producto(lista):
 #   product=1
 #   for numero in lista:
 #       product *= numero
 #   print(f"El producto de la lista es: {product}")

#lista=crearlista()
#producto(lista)
#corregido
def crearlista(longitud):
    cont=0
    lista=[]
    while cont < longitud:
        entrada = int(input(f'Introduce el valor de la posicion {cont +1}'))
        lista.append(int(entrada))
        cont+=1
    return lista

def proc2lista():
    longitud=int(input("Escribe la longitud del a lista"))
    lista1=crearlista(longitud)
    lista2=crearlista(longitud)

    listaMax=[]
    
    for i,j in zip(lista1,lista2):
        listaMax.append(i*j)
    print(f"Lista1: {lista1}")
    print(f"Lista2: {lista2}")
    print(f"El valor del producto de las listas es: {listaMax}")

proc2lista()
