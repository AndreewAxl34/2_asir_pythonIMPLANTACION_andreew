#Introducir valores numericos en una listam, maximo
#5 valores, de forma ascedentence, no se guarda en al lista osea igual, 
#mayor o menor del ultimo grabado
#datos
def datoslista():
    lista=[]
    #pediremos un numero para que no este vacia la lista
    primero=int(input("Introduce el primer numero: "))
    lista.append(primero)
    for i in range(4):
        numeros=int(input("introduce_numero"))
        # este  bucle servira para comparar de manera ascendente
        if numeros > lista[-1]:
           lista.append(numeros)
    return lista

def visualizar(lista):
    print(f"La lista tiene de valores: {lista}")

#funciones
lista=datoslista()
visualizar(lista)
