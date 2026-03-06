# 10 .-Solicitar el ingreso de una clave por teclado y almacenarla en una
# cadena de caracteres. Controlar
# que el string ingresado tenga entre 10 y 20 caracteres para que sea válido,
# en caso contrario mostrar un
# mensaje de error
texto=input("Ingresa una clave por teclado")

cantidad=len(texto)

if cantidad <= 20 and cantidad >= 10:
    print(f"El texto ingresado es valido, ya que tiene {cantidad} caracteres ")
else:
    print("Error")

