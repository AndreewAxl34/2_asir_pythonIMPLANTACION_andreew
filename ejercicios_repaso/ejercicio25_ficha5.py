#25.- En una empresa se almacenaron los sueldos de 10 personas.
#Desarrollar las siguientes funciones y llamarlas 
#desde el bloque principal:
#1) Carga de los sueldos en una lista.
#2) Impresión de todos los sueldos.
#3) Cuántos tienen un sueldo superior a $4000.
#4) Retornar el promedio de los sueldos.
#5) Mostrar todos los sueldos que están por debajo del promedio. 

def cargarsueldos():
    sueldos=[]
    for i in range(10):
        sueldo=int(input("Escribe un sueldo: "))
        sueldos.append(sueldo)
    return sueldos

def imprimir(sueldos):
    print(sueldos)

def cantidad4000(sueldos):
    cont=0
    for sueldo in sueldos:
        if(sueldo > 4000):
            cont+=1
    print(f"La cantidad de sueldos mayores a 4000 son: {cont}")

def promedio(sueldos):
    suma = 0
    promedios = 0
    for i in range(len(sueldos)):
        suma += sueldos[i]
        promedios = suma / len(sueldos)
    return promedios

def devolver(sueldos,promedios):
    print(f"El promedio de los sueldos es: {promedios}")
    for sueldo in sueldos:
        if(sueldo < promedios):    
           print(f"Los sueldos menores del promedio son: {sueldo} ") 

sueldos=cargarsueldos()
promedios=promedio(sueldos)
imprimir(sueldos)    
cantidad4000(sueldos)   
devolver(sueldos,promedios)
