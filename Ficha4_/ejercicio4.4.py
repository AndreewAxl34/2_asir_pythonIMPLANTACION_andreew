#4.- Definir por asignación una lista con 8
#elementos enteros. Contar cuantos de dichos valores
#almacenan un valor superior a 100.
lista=[]
cont=0
for i in range(8):
           valor=int(input("escribimos el valor"))
           lista.append(valor)
           if (valor > 100):
             cont+=1
print(cont)
               
