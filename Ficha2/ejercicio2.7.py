#7.- En una empresa trabajan n empleados cuyos sueldos
#oscilan entre $100 y $500, realizar un programa que lea los
#sueldos que cobra cada empleado e informe cuántos empleados
#cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa
#deberá informar el importe que gasta la empresa en sueldos al personal.
numero_empleados=int(input("Escribe el numero de empleados: "))
total=0
sueldobajo=0
cont=1
while cont <= numero_empleados:
        sueldos=float(input("Escribe un sueldo aproximado: "))
        if sueldos >= 100 and sueldos <=500:
            cont=cont+1
            total=total+sueldos
            if sueldos <=300:
                sueldobajo+=1
        else:
             print("mete una cantidad netre 100 y 500 ")
             
print(f"El numero de sueldos entre 100 y 300 son {sueldobajo }")
print(f"El numero de sueldos mayor que 300 son {numero_empleados-sueldobajo }")
print(f"El total que tiene que pagar la empresa es {total }")
   
 
        

