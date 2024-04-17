# edad = int(input("Ingrese su edad: "))
# for i in range (edad,0,-1):
#     print(i)

tamaño = int(input("Ingrese un numero impar: "))
m = tamaño // 2
for i in range (1,m+1):
    print(" "*(m-i), "*" *(2*i-1))
print("*"*tamaño)
for i in range (m,0,-1):
    print(" "*(m-i), "*" *(2*i-1))