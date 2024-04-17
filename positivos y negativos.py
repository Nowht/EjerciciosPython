#Ejercicio 9
positivo = 0
negativo = 0
promedio = 0
for i in range(0,6):
    num = int(input("Ingresa un numero positivo o negativo: "))
    if num >= 1:
        positivo = positivo + num
        promedio = promedio + 1
    else:
        negativo = negativo + num

if positivo == 0 and promedio == 0:
    print("No hay numeros positivos")
else:
    print("\nPromedio de los Numeros Positivos:", (positivo//promedio))
print("Suma de los Numeros Negativos:", negativo,"\n")