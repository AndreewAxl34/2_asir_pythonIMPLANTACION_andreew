#9.- Ingresar una oración que pueden tener letras tanto
#en mayúsculas como minúsculas. Contar la cantidad de vocales.
#Crear un segundo string con toda la oración en minúsculas
#para que sea más fácil disponer la condición que
#verifica que es una vocal.
oracion=input("Ingresa una oracion con tanto mayusculas como minusculas: ")
oracion2=oracion.lower()
print(f'segunda frase: {oracion2}')
vocales="aeiou"

resultado1=0
resultado2=0

for caracteres in oracion:
     if caracteres in vocales:
         resultado1+=1


for caracteres in oracion2:
     if caracteres in vocales:
         resultado2+=1

print(f"En la primer oracion hay: {resultado1} vocales \n En las segunda oracion hay: {resultado2} vocales")

    





