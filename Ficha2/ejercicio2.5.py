#5.- Escribir un programa que solicite ingresar
#10 notas de alumnos y nos informe cuántos tienen
#notas mayores o iguales a 7 y cuántos menores. 
#nota=int(input("ingresa la nota de un alumno: ")
#for i in range(1,nota+1)
#corregido
valores=int(input("ingresa la numero de notas: "))
mayores=0
for i in range(1,valores+1):
     nota=int(input(" Introduce la nota(1): "))
     if nota>=7:
        mayores+=1
print(f"El numero de notas mayores de 7  son: {mayores}")
print(f"El numero de notas menores de 7  son: {valores-mayores")
