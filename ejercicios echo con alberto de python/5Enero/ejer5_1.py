#Declarar 2 listas con valores numericos, ambas del mismo tamaño, 
#si no son el mismo tamaño, da error
# obtener otra lista con aquellos valores que esten 
#en ambas listas y en la misma posicion
#------DATOS---------------
lista1=[1,7,7,7]
lista2=[4,7,7,7]
#------FUNCIONES---------------
def comparacion(lista1,lista2):
     lista_conjunta=[]
     if(len(lista1) != len(lista2)):
        print("Error")
     else:
        for i in range(len(lista1)):
             if (lista1[i]==lista2[i]):
                   lista_conjunta.append(lista1[i])
     return lista_conjunta
 
def visualizar(resultado):
     print(f"El resultado es: {resultado}")
        
#---------PROGRAMA PRINCIPAL---
resultado=comparacion(lista1,lista2)
visualizar(resultado)
