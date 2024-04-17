day = int(input("Ingrese dia: "))
month = int(input("Ingrese mes: "))
year = int(input("Ingrese año: "))

if year > 9999 or year < 999:
    print("Año Incorrecto")

elif(year%4 == 0) and (year%100 != 0) or (year%400 == 0): #Si es Bisiesto
    if month <= 12:
        if (month == 1 and day <= 31) or (month == 3 and day <= 31) or (month == 5 and day <= 31) or (month == 7 and day <= 31) or (month == 8 and day <= 31) or (month == 10 and day <= 31) or (month == 12 and day <= 31) or (month == 4 and day <= 30) or (month == 6 and day <= 30) or (month == 9 and day <= 30) or (month == 11 and day <= 30) or (month == 2 and day <= 29): #comparando meses con sus respectivos dias
            print("Fecha Valida")
        else:
            print("Dia invalido")
    else:
        print("Mes invalido")

elif(year%4 != 0) and (year%100 == 0) or (year%400 != 0): #No es bisiesto
    if month <= 12:
        if (month == 1 and day <= 31) or (month == 3 and day <= 31) or (month == 5 and day <= 31) or (month == 7 and day <= 31) or (month == 8 and day <= 31) or (month == 10 and day <= 31) or (month == 12 and day <= 31) or (month == 4 and day <= 30) or (month == 6 and day <= 30) or (month == 9 and day <= 30) or (month == 11 and day <= 30) or (month == 2 and day <= 28): #comparando meses con sus respectivos dias
            print("Fecha Valida")
        else:
            print("Dia invalido")
    else:
        print("Mes invalido")

