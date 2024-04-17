gastado = int(input("Ingrese el valor gastado: "))
billete = int(input("Ingrese el billete: "))

vuelto = billete - gastado

x1 = vuelto // 10
x2 = vuelto % 10

if gastado == billete:
    print("no hay vuelto")

if x1 >= 6:
    q = 5 % x1
    q1 = x1 % 5
    if q >= 5:
        q = 1
        print(q,"Billetes de Q50")
        if q1 %2==0:
            q1 = q1 //2
            print(q1,"Billetes de Q20")
        else:
            q1 = q1 // 2
            n = q1 % 2
            q1 = 1
            print(q1,"Billetes de Q20")
            print(n,"Billetes de Q10")
        if x2 >= 5:
            r = 5 % x2
            r1 = x2 % 5
            if r >= 5:
                r = 1
                print(r,"Billetes de Q5")
                if r1 >= 5:   
                    print(r1,"Monedas de Q1")
        if x2 >= 1 and x2 <= 4:
            print(x2,"Monedas de Q1")

if x1 >= 1 and x1 <= 4:
    if x1 %2==0:
        x1 = x1 // 2
        print(x1,"Billetes de Q20")
    else:
        x1 = x1 // 2
        n = x1 % 2
        x1 = 1
        print(x1,"Billetes de Q20")
        print(n,"Billetes de Q10")
    if x2 >= 5:
        i = x2
        r = 5 % x2
        r1 = x2 % 5
        if r >= 5 or i == 5:
            r = 1
            print(r,"Billetes de Q5")
            if r1 >= 5:   
                print(r1,"Monedas de Q1")
    if x2 >= 1 and x2 <= 4:
        print(x2,"Monedas de Q1")
       

if x1 == 5:
   x1 = 1
   print(x1,"Billetes de Q50")
   if x2 >= 5:
        r = 5 % x2
        r1 = x2 % 5
        if r >= 5:
            r = 1
            print(r,"Billetes de Q5")
            if r1 >= 5:   
                print(r1,"Monedas de Q1")
   if x2 >= 1 and x2 <= 4:
       print(x2,"Monedas de Q1")