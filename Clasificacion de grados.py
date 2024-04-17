e0 = int(input("Ingrese una edad 1: "))
e1 = int(input("Ingrese una edad 2: "))
e2 = int(input("Ingrese una edad 3: "))
e3 = int(input("Ingrese una edad 4: "))
e4 = int(input("Ingrese una edad 5: "))
e5 = int(input("Ingrese una edad 6: "))
e6 = int(input("Ingrese una edad 7: "))
e7 = int(input("Ingrese una edad 8: "))
e8 = int(input("Ingrese una edad 9: "))
e9 = int(input("Ingrese una edad 10: "))

prekinder = 0
kinder = 0
Preparatoria = 0

if (3<e0<=6) and (3<e1<=6) and (3<e2<=6) and (3<e3<=6) and (3<e4<=6) and (3<e5<=6) and (3<e6<=6) and (3<e7<=6) and (3<e8<=6) and (3<e9<=6):
    if e0 == 4:
        prekinder += 1
    if e1 == 4:
        prekinder += 1
    if e2 == 4:
        prekinder += 1
    if e3 == 4:
        prekinder += 1
    if e4 == 4:
        prekinder += 1
    if e5 == 4:
        prekinder += 1
    if e6 == 4:
        prekinder += 1
    if e7 == 4:
        prekinder += 1
    if e8 == 4:
        prekinder += 1
    if e9 == 4:
        prekinder += 1

    if e0 == 5:
        kinder += 1
    if e1 == 5:
        kinder += 1
    if e2 == 5:
        kinder += 1
    if e3 == 5:
        kinder += 1
    if e4 == 5:
        kinder += 1
    if e5 == 5:
        kinder += 1
    if e6 == 5:
        kinder += 1
    if e7 == 5:
        kinder += 1
    if e8 == 5:
        kinder += 1
    if e9 == 5:
        kinder += 1

    if e0 == 6:
        Preparatoria += 1
    if e1 == 6:
        Preparatoria += 1
    if e2 == 6:
        Preparatoria += 1
    if e3 == 6:
        Preparatoria += 1
    if e4 == 6:
        Preparatoria += 1
    if e5 == 6:
        Preparatoria += 1
    if e6 == 6:
        Preparatoria += 1
    if e7 == 6:
        Preparatoria += 1
    if e8 == 6:
        Preparatoria += 1
    if e9 == 6:
        Preparatoria += 1

    print("Para prekinder hay: ",prekinder)
    print("Para prekinder hay: ",kinder)
    print("Para prekinder hay: ",Preparatoria)    

else:
    print("Error")    
