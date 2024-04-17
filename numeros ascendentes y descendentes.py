a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

if a >= b and a >= c:
    if c >= b:
        print("Orden Ascendente: ", a,",",c,",",b)
        print("Orden Descendente: ", b,",",c,",",a)
    elif b >= c:
        print("Orden Ascendente: ", a,",",b,",",c)
        print("Orden Descendente: ", c,",",b,",",a)

elif b >= a and b >= c:
    if c >= a:
        print("Orden Ascendente: ", b,",",c,",",a)
        print("Orden Descendente: ", a,",",c,",",b)
    elif a >= c:
        print("Orden Ascendente: ", b,",",a,",",c)
        print("Orden Descendente: ", c,",",a,",",b)

elif c >= a and c >= b:
    if a >= b:
        print("Orden Ascendente: ", c,",",a,",",b)
        print("Orden Descendente: ", b,",",a,",",c)
    elif b >= a:
        print("Orden Ascendente: ", c,",",b,",",a)
        print("Orden Descendente: ", a,",",b,",",c)