#6.- Definir una lista que almacene por
#asignación los nombres de 5 personas. Contar cuantos de esos
#nombres tienen 5 o más caracteres.
lista=[]
cont=0
for i in range(5):
        nombre=input("escribe el nombre: ")
        lista.append(nombre)
        for elemento in lista:
             if (len(elemento) >=5):
                 cont+=1
print(f"Los nombre que tienen 5 o mas caracteres son {cont}")




