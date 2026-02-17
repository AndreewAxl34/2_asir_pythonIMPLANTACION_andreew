#Una lsita el cual nos comenta los 
#datos de un alumno:Nombre,curso, y sus notas, diccionario
#Se pide su nota media, y el nombre del alumno
#--------DATOS------------------------
alumno={
    "Nombre":"Andreew",
    "Curso":"2ºASIR",
    "NOTAS":[7,6,7]
}

#---------FUNCIONES--------------------
def proceso(alumno):
        notas=alumno["NOTAS"]
        suma=0
        for i in notas:
           suma+=i
        media=suma/len(notas)
        return media

def visualizar(alumno,resultado):
    print(f"EL alumno: {alumno['Nombre']}, tiene de nota media: {resultado}")


#--------PROGRAMA PRINCIPAL-------------
resultado=proceso(alumno)
visualizar(alumno,resultado)



