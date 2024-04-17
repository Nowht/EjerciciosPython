ingreso = float(input("ingrese la cantidad: "))
impuesto = ingreso*18/100 - 556.02 
if ingreso > 85528: 
    print("Impuesto a pagar: ", round(14839+(ingreso-85528)*32/100,1))

elif ingreso < 85528:
    if impuesto > 0:
        print("Impuesto a pagar: ", round(impuesto,1))
    else:
        print("El impuesto a pagar es: 0")