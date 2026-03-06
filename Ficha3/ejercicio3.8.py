#8.- Cargar una oración por teclado. Mostrar luego
#cuantos espacios en blanco se ingresaron. Tener en
#cuenta que un espacio en blanco es igual a " ", en
#cambio una cadena vacía es ""
oracion=input("Escribe una oracion: ")
numero_espacios=oracion.count(" ");
print(f"En la oracion: {oracion} \n hay un total de espacios de: {numero_espacios}")
