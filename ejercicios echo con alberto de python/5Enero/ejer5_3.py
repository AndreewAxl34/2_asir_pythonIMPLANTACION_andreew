#Una lista compuesta por diferentes diccionarios,
# ver quien de los alumnos tiene mas nota media
alumnos=[
    {
    "Nombre":"Andreew",
    "Curso":"2ºASIR",
    "NOTAS":[5,7,7]
    },
     {
    "Nombre":"Sara",
    "Curso":"1ºASIR",
    "NOTAS":[7,5,8]
    },
     {
    "Nombre":"Alberto",
    "Curso":"2ºASIR",
    "NOTAS":[7,7,7]
    }
]
#-----------FUNCIONES-------------------
def proceso(alumnos):
      for alum in alumnos:
        suma=0
        notas=alum["NOTAS"]
        for i in notas:
            suma+=i
        media=suma/len(notas)
        if(media > media):
         resultado=media

def visualizar(resultado,alumnos):
    for alum in alumnos:
        print(f"El alumno: {alum['Nombre']}, tiene la media mas alta: {resultado}")

#-------------PROGRAMA PRINCIPAL---------
resultado=proceso(alumnos)
visualizar(resultado,alumnos)




