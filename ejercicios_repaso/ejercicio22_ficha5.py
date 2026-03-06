# 22.- Confeccionar una función que cargue por teclado una 
# lista de 5 enteros y la retorne. Una segunda función 
# debe recibir una lista y mostrar todos los valores mayores
# a 10. Desde el bloque principal 
# del programa llamar a ambas funciones.
def crearlista():
    lista=[]
    for i in range(5):
        numero=int(input("Escribe un numero: "))
        lista.append(numero)
    return lista

def funcion(lista):
    mayor=[]
    for numero in lista:
        if(numero > 10):
            mayor.append(numero)
    print(f"Los numeros mayores de 10 son: {mayor}")

lista=crearlista()
funcion(lista)
