cursos=[]
notas=[]

cantidad_cursos = int(input("Ingrese la cantidad de cursos: "))

for i in range(cantidad_cursos,0,-1):
    curso = input("Ingrese el nombre del curso: ")
    cursos.append(curso)
    notass = int(input("Ingrese la nota del curso: "))
    notas.append(notass)

print("")
print("Cursos: ",cursos)
print("Notas: ",notas,"\n")