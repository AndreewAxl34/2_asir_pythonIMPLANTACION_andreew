# 37.- Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene
# como dato las temperaturas medias mensuales de dichos paises.
# Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias
# mensuales.
# Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en
# memoria.
# a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
# b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las
# mismas.
# c - Calcular la temperatura media trimestral de cada país.
# c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
# b - Imprimir el nombre del pais con la temperatura media trimestral mayor.

#paises=[]

#for i in range(4):
#       pais=input("Escribe 4 paises: ")
#       temperaturas=[]
 #      for i in range(3):
#              tempe=float(input("Escribe la temperatura: "))
#              temperaturas.append(tempe)
 #      paises.append([pais,temperaturas])

#print(f"Imprimir los nombres y las temperaturas: {paises}")

#for i in range(len(paises)):
 #      suma=0
 #      mediamayor=0
#       for j in range(len(temperaturas)):
#              suma+=temperaturas[j]
 #             media=suma/3
 #      if(media > temperaturas[j]):
 #         mediamayor=media

#print(f"La media de las temperaturas de {paises[i][0]} es: {media}")
#print(f"La media mayor es {mediamayor} y es del pais {paises[i][0]}")
# corregido
paises=[]

for i in range(4):
       pais=input("Escribe 4 paises: ")
       temperaturas=[]
       for i in range(3):
              tempe=float(input("Escribe la temperatura: "))
              temperaturas.append(tempe)
       paises.append([pais,temperaturas])

for p in paises:
      print(f"Pais: {p[0]} | Temperaturas: {p[1]}")

nombre_mayor=""
mediamayor=-999
for i in range(len(paises)):
    suma=0
    nombre_actual= paises[i][0]
    lista_temp= paises[i][1]
    
    for j in range(len(lista_temp)):
          suma += lista_temp[j]
    media = suma/3
    print(f"La media de {nombre_actual} es: {media}")

    if media > mediamayor:
          mediamayor = media
          nombre_mayor = nombre_actual
          
print(f"La media mayor es {mediamayor} y es del pais {nombre_actual}")


