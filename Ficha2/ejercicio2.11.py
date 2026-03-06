#11.-Desarrollar un programa que permita cargar n números enteros y
#luego nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional
#(este operador retorna el resto de la división de dos valores,
#por ejemplo 11%2 retorna un 1):if valor%2==0:   
valor=int(input("Escribe un valor: "))
count=1
pares=0;
#while count <= valor:
#        if valor%2==0:
#         count=count+valor
#         print(f"El numero de valores pares son: {count}")
#        elif valor%3==0:
#         count=count+valor
#         print(f"El numero de valores pares son: {count}")
#        else:
#            print("error")
# corregido
while count <= valor:
    numero=int(input("Introduce el valor: "));
    if numero%2==0:
        pares+=1
    count+=1
print(f"El numero de numeros pares es: {pares}")
print(f"El numero de numeros impares es: {valor-pares}")
