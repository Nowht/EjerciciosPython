titulo_ = []
autor_ = []
categoria_ = []
año_de_publicacion = []

def agregar():
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    categoria = input("Ingrese la categoria del libro: ")
    año = int(input("Ingrese el año de publicacion: "))

    titulo_.append(titulo)
    autor_.append(autor)
    categoria_.append(categoria)
    año_de_publicacion.append(año)
    print("")

def buscartitulo():
    titulo = input("Ingrese el titulo del libro que desea buscar: ")
    if titulo in titulo_:
        indice = titulo_.index(titulo)
        print(f"Titulo: {titulo_[indice]} | Autor: {autor_[indice]} | Categoria: {categoria_[indice]} | Año de Publicacion: {año_de_publicacion[indice]}")
        print("")          

def buscarautor():
    autor = input("Ingrese el autor del libro que desea buscar: ")
    if autor in autor_:
        indice = autor_.index(autor)
        print(f"Titulo: {titulo_[indice]} | Autor: {autor_[indice]} | Categoria: {categoria_[indice]} | Año de Publicacion: {año_de_publicacion[indice]}")
        print("")          

def buscarcategoria():
    categoria = input("Ingrese la categoria del libro que desea buscar: ")
    if categoria in categoria_:
        indice = categoria_.index(categoria)
        print(f"Titulo: {titulo_[indice]} | Autor: {autor_[indice]} | Categoria: {categoria_[indice]} | Año de Publicacion: {año_de_publicacion[indice]}") 
        print("")      

def eliminar():
    titulo = input("Ingrese el titulo del libro que desea eliminar: ")
    if titulo in titulo_:
        indice = titulo_.index(titulo)
        titulo_.pop(indice)
        autor_.pop(indice)
        categoria_.pop(indice)
        año_de_publicacion.pop(indice)
        print("")


def mostrar():
    for i in range(0,len(titulo_)):
        print(f"Titulo: {titulo_[i]} | Autor: {autor_[i]} | Categoria: {categoria_[i]} | Año de Publicacion: {año_de_publicacion[i]}")
        print("")   

intentos = 3
user = input("Ingrese el usuario: ")
pswd = input("Ingrese la contraseña: ")
while pswd != "contraseña" or user != "usuario9" and intentos !=0:
    print("Intentos: ",intentos)
    user = input("Ingrese el usuario: ")
    pswd = input("Ingrese la contraseña: ")
    intentos -= 1

if intentos == 0:
    print("Demasiados intentos")    

while pswd == "contraseña" and user == "usuario9":
    print("1. Agregar un libro\
           \n2. Buscar un libro por titulo\
           \n3. Buscar libro por autor\
           \n4. Buscar Libro por categoria\
           \n5. Eliminar Libro\
           \n6. Mostrar todos los libros\
           \n7. Salir")
    opcion = int(input("\nIngrese una opcion: "))
    print("")

    if opcion == 1:
        agregar()
    if opcion == 2:
        buscartitulo()
    if opcion == 3:
        buscarautor()
    if opcion == 4:
        buscarcategoria()
    if opcion == 5:
        eliminar()
    if opcion == 6:
        mostrar()
    if opcion == 7:
        break