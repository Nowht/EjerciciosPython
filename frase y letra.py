#ejercicio 7
frase = input("Ingrese un frase: ")
letra = input("Ingrese una letra: ")
veces = 0

for i in frase:
    if i == letra:
        veces = veces + 1
print(veces)