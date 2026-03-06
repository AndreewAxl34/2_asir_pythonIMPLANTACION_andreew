#6.- Se ingresan un conjunto de n alturas ç
#de personas por teclado. Mostrar la altura promedio de las personas.
#valores=int(input("Ingresa un conjunto numero de alturas")
#altura=0
#for i in range(1,altura+1)
#      suma=altura
alturas=int(input("Introduce el numero de alturas: "))
cont=1
suma=0
while cont<=alturas:
    valor=float(input("Introduce le valor: "))
    suma=suma+valor
    cont=cont+1
print(f"El valor promedio de las alturas es: {suma/alturas}")
