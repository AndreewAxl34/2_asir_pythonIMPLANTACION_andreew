#1 .-Realizar la carga por teclado del nombre,ç
#edad y altura de dos personas. Mostrar por pantalla el
#nombre de la persona con mayor altura.

Persona1=input("Escribe el nombre de la primera persona: ")
edad1=int(input("Escribe la edad de la primera persona: "))
altura1=float(input("Escribe la altura de la primera persona: "))

Persona2=input("Escribe el nombre de la segunda persona: ")
edad2=int(input("Escribe la edad de la segunda persona: "))
altura2=float(input("Escribe la altura de la segunda persona: "))

if altura1 > altura2:
     print(f"La altura de {Persona1} 1 es mayor \n porque su altura es: {altura1}")
elif altura2 > altura1:
     print(f"La altura de {Persona2} 2 es mayor \n porque su altura es: {altura2}")
else:
     print("La altura son iguales")
