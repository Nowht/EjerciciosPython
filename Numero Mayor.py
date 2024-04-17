n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
n3 = int(input("Ingrese un numero: "))

if n1 == n2 == n3:
    print("Todos son iguales")   

elif n1 >= n2 and n1 >= n3:
    print("el numero mayor es: ",n1)
elif n2 >= n1 and n2 >= n3:
    print("el numero mayor es: ",n2)
elif n3 >= n1 and n3 >= n2:
    print("el numero mayor es: ",n3)

if n1 <= n2 and n1 <= n3:
    print("el numero menor es: ",n1)
elif n2 <= n1 and n2 <= n3:
    print("el numero menor es: ",n2)
elif n3 <= n1 and n3 <= n2:
    print("el numero menor es: ",n3)    