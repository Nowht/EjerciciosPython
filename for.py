# edad = int(input("Ingrese su edad: "))
# for i in range (edad,0,-1):
#     print(i)

# tamaño = int(input("Ingrese un numero impar: "))
# m = tamaño // 2
# for i in range (1,m+1):
#     print(" "*(m-i), "*" *(2*i-1))
# print("*"*tamaño)
# for i in range (m,0,-1):
#     print(" "*(m-i), "*" *(2*i-1))

# for i in range(1,6):
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print("")

inicio = int(input("Ingrese la tabla a iniciar: "))
final = int(input("Ingrese la tabla a finalizar: "))
limite = int(input("Ingrese el limite a llegar: "))

for i in range (1,limite+1):
    for x in range(inicio,final+1):
        print(x,"*",i,"=",i*x,end="\t")
    print("")