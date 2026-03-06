#2 .-Realizar la carga de dos nombres por teclado.
#Mostrar cual de los dos es mayor alfabéticamente o si
#son iguales.

nombre1=input("Escribe el primer nombre: ")

nombre2=input("Escribe el segundo nombre: ")

if nombre1 > nombre2:
    print(f"El nombre1 es mayor porque su valor es: {nombre1}") 
elif nombre2 > nombre1:
    print(f"El nombre2 es mayor porque su valor es: {nombre2}") 
else:
    print("Ambos son iguales") 
