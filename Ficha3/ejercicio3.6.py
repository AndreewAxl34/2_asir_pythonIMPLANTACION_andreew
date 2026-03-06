#6.-Solicitar la carga del nombre de una persona en minúsculas.
#Mostrar un mensaje si comienza con
#vocal dicho nombre.
nombre = input("escribe un nombre: ")
primera_letra_minusculas=nombre[0].lower()
vocales = "aeiou"
if primera_letra_minusculas in vocales:
    print(f"El nombre empieza por una vocal porque se llama: {nombre}")
else:
    print(f"El nombre NO empieza por una vocal porque se llama: {nombre}")
