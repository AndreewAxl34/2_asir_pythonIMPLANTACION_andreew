#10.- Cargar por teclado y almacenar en una lista las
#alturas de 5 personas (valores float)
#Obtener el promedio de las mismas. Contar cuántas
#personas son más altas que el
#promedio y cuántas más bajas.
#lista=[]
#cont=0
#for i in range(5):
#         altura=float(input("Escribe la altura "))
#         lista.append(altura)
#         cont+=1
#         for elemento in lista:
#             cantidad=len(lista)
#             suma=elemento+elemento
#             promedio=suma/cantidad
 #        if altura > promedio:
#             cont=+1
#             altas=cont
#         elif altura < promedio:
#              cont=+1
#              bajas=cont
#print(f"La lista de la altura es: {lista}")
#print(f"El promedio de las alturas es: {promedio}")
#print(f"La cantidad de personas altas que el promedio son: {altas}")
#print(f"La cantidad de personas bajas que el promedio son: {bajas}")

lista=[]
suma=0
mayor=0
menor=0
igual=0
for i in range(5):
         altura=float(input("Escribe la altura "))
         lista.append(altura)
         suma+=altura
         promedio=suma/len(lista)

for elemento in lista:
    if elemento > promedio:
        mayor+=1
    elif elemento < promedio:
        menor+=1
    else:
        igual+=1

print(f"La lista de la altura es: {lista}")
print(f"El promedio de las alturas es: {promedio}")
print(f"La cantidad de personas altas que el promedio son: {mayor}")
print(f"La cantidad de personas bajas que el promedio son: {menor}")
print(f"La cantidad de personas igual al promedio son: {igual}")


