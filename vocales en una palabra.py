word = []
vocales = ["a","e","i","o","u"]

palabra = input("Ingrese una palabra: ")

for i in palabra:
    word.append(i)

for x in vocales:
    if word.count(x) > 0:
        print("Veces que se repite la letra",x,": ",word.count(x)) 