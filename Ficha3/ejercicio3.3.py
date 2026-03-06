#3.- Realizar la carga de enteros por teclado. 
#Preguntar después que ingresa el valor si desea cargar otro
#valor debiendo el operador ingresar la cadena 'si' o 'no'
#por teclado. Mostrar la suma de los valores ingresados.
##texto1=int(input("Ingresa un valor: "))
##if texto1:
##    opcion=(input("Ingresa la Opcion n\ 1)Si \n 2)no: "))
##    if opcion == "Si":
##        texto2=int(input("ingresa otro valor: "))
##        suma=texto1+texto2
##        print(f"Has ingresado el: \n valor1:{texto1} \n valor2:{texto2} \n la suma de valores ingresados es: {suma}")
##    elif opcion == "No":
##        print(f"Has ingresado el: \n valor1:{texto1}")
##    else:
##        print("error")
## corregido
suma=0
while input("quieres seguir si/no: ") == "si":
     valor=int(input("introduce un valor: "))
     suma+=valor
print(suma)
