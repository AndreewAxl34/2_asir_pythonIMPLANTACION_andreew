#4.- Una planta que fabrica perfiles de hierro posee un lote de n piezas.
#Confeccionar un programa que pida ingresar por teclado la cantidad de
#e piezas a procesar y luego ingrese la longitud de cada perfil;
#sabiendo que la pieza cuya longitud esté comprendida en el
#rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad
#de piezas aptas que hay en el lote. 
#pieza=int(input("Introduce la cantidad de piezas"))
#count=1
#while count<=pieza:
#      medida_perfil=int(input("Introduce el numero de piezas"))
#      if ( medida_perfil >= 1,20 and  medida_perfil <= 1,30):
#            buenas=buenas+1
#print("las numero de perfiles buenos son: (buenas)")           
#print("las numero de perfiles mallos son:  malos(buenas)")
# corregido
pieza=int(input("Introduce la cantidad de piezas: "))
buenas=0
for i in range (1,pieza+1):
     medida=float(input("Introduce el numero de medida: "))
     if medida>=1.20 and medida<=1.30:
        buenas+=1
print(f"las numero de perfiles buenos son: {buenas}")           
print(f"las numero de perfiles mallos son:  {pieza-buenas}")   
