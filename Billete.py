ingresado_separado = []

def decena():
    decena = int(ingresado_separado[0])
    d2 = decena % 5     #Separa los numeros restantes de 5
    if decena >= 5:
        d1 = 5 % decena     #Separa el 5 de los numeros restantes
        if decena == 5 or d1 == 5:
            print(1,"Billete de Q50")
        if d2 > 1:
            print(d2//2,"Billetes de Q20")
        if d2 == 1 or d2 == 3:
            print(1,"Billetes de Q10")
    else:
        if d2 > 1:
            print(d2//2,"Billetes de Q20")
        if d2 == 1 or d2 == 3:
            print(1,"Billetes de Q10")

def unidad():
    unidad = int(ingresado_separado[1])
    if unidad >= 5:
        u1 = 5 % unidad
        u2 = unidad % 5
        if unidad == 5 or u1 == 5:
            print(1,"Billete de Q5")
        if unidad >= 5 and u2 != 0:
            print(u2,"Monedas de Q1")
    if unidad <= 4 and unidad != 0:
        print(unidad,"Monedas de Q1")

def decimales():
    decimal1 = int(ingresado_separado[2])
    decimal2 = int(ingresado_separado[3])

    if decimal2 != 0:
        ctv1 = 5 % decimal2     #Separa 5 de los numeros restantes centavos
        ctv2 = decimal2 % 5     #Separa los numeros restantes del 5

    dl2 = decimal1 % 5
    if decimal1 >= 5:
        dl1 = 5 % decimal1
        if decimal1 == 5 or dl1 == 5:
            print(1,"Monedas de Q0.50")
        if dl2 >= 2 and (decimal2 >= 5 or decimal1 == 9) or decimal1 == 8:
            print(1,"Monedas de Q0.25")
        if dl2 == 1 or (dl2 == 4 and decimal2 != 5) or (dl2 == 3 and decimal2 != 0):
            print(1,"Monedas de Q0.10")
        if dl2 == 4 and decimal2 == 5 or (decimal1 == 7 and decimal2 < 5):
            print(2,"Monedas de Q0.10")
        if decimal1 >= 7 and (decimal2 == 0 and decimal1 != 7) or (decimal1 == 6 and decimal2 >= 5):
            print(1,"Monedas de Q0.5")
    
    else:
        if decimal1 >= 2 and (decimal2 >= 5 or decimal1 == 3) or decimal1 == 4:
            print(1,"Monedas de Q0.25")
        if decimal1 == 1 or (decimal1 == 2 and decimal2 != 0 and decimal2 != 5) or (decimal1 == 4 and decimal2 == 0) or (decimal1 == 3 and decimal2 != 0):
            print(1,"Monedas de Q0.10")
        if (decimal1 == 2 and decimal2 == 0) or (decimal1 == 4 and decimal2 >= 5):
            print(2,"Monedas de Q0.10")
        if (decimal2 == 5 and decimal1 != 4) or (decimal1 == 1 and decimal2 == 5) or (decimal1 == 3 and decimal2 == 0):
            print(1,"Monedas de Q0.05")

    if decimal2 >= 6 and decimal2 !=0:
        print(ctv2,"Monedas de Q0.01")
    if decimal2 >=1 and decimal2 <= 4:
        print(ctv2,"Monedas de Q0.01") 

def centena():
    nueva = ingresado_separado[:]
    for i in range (1,4):
        nueva.pop()
    centena = int(nueva[0])
    if centena % 2 == 0:
        print(centena//2,"Billetes de Q200")
    if centena % 2 != 0 and centena != 1:
        print(centena//2,"Billetes de Q200")
        print(1,"Billete de Q100")
    if centena == 1:
        print(1,"Billete de Q100")

ingresado = float(input("Ingrese un Numero: "))

for i in str(ingresado):
    if i != ".":
        ingresado_separado.append(i)

digitos = len(ingresado_separado)

if float(ingresado) <= 9:
    ingresado_separado.insert(0, 0)
    unidad()
    if digitos == 2:
        ingresado_separado.append(0)
        decimales()
    if digitos == 3:
        decimales()             

elif float(ingresado) <= 99:
    if digitos == 3:
        ingresado_separado.append(0)
    decena()
    unidad()
    decimales()

elif float(ingresado) >= 100:
    centena()
    ingresado_separado.pop(0)
    decena()
    unidad()
    if digitos == 5:
        decimales()
    if digitos == 4:
        ingresado_separado.append(0)
        decimales()