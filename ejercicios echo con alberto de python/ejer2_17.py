#Crear una superlista osea lista de listas
#en cotenga 5 listas
# cada una de esas sublistas se crean igual que el ejercicio anterior
def superlista():
    megalistas=[]
    for i in range(5):
        listas=[]
        #pediremos un numero para que no este vacia la lista
        primero=int(input("Introduce el primer numero: "))
        listas.append(primero)
        for j in range(4):
          numeros=int(input("introduce_numero"))
           # este  bucle servira para comparar de manera ascendente
          if numeros > listas[-1]:
             listas.append(numeros)
        megalistas.append(listas)
    return megalistas

def visualizar(megalistas):
    print(f"La lista tiene de valores: {megalistas}")

#funciones
megalistas=superlista()
visualizar(megalistas)
