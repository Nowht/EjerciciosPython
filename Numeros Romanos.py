def romano1_9(numero):
    if numero <= 3:
        print(numero, "en romanos es","I"*numero)
    if numero == 4:
        print(numero, "en romanos es","IV")
    if numero >= 5 and numero <= 8:
        number = numero % 5
        print(numero, "en romanos es","V","I"*number)
    if numero == 9:
        print(numero, "en romanos es","IX") 

def romano10_19(numero):
    number = numero % 10
    if numero <= 13:
        print(numero, "en romanos es","X","I"*number)
    if numero == 14:
        print(numero, "en romanos es","XIV")

    number2 = number % 5    
    if numero >= 15 and numero <= 18:
        print(numero, "en romanos es","XV","I"*number2)
    if numero == 19:
        print(numero, "en romanos es","XIX")

def romano20_29(numero):
    number = numero % 20
    if numero <= 23:
        print(numero, "en romanos es","XX","I"*number)
    if numero == 24:
        print(numero, "en romanos es","XXIV")

    number2 = number % 5    
    if numero >= 25 and numero <= 28:
        print(numero, "en romanos es","XXV","I"*number2)
    if numero == 29:
        print(numero, "en romanos es","XXIX")    

def romano30_39(numero):
    number = numero % 30
    if numero <= 33:
        print(numero, "en romanos es","XXX","I"*number)
    if numero == 34:
        print(numero, "en romanos es","XXXIV")

    number2 = number % 5    
    if numero >= 35 and numero <= 38:
        print(numero, "en romanos es","XXXV","I"*number2)
    if numero == 39:
        print(numero, "en romanos es","XXXIX")    

def romano40_49(numero):
    number = numero % 40
    if numero <= 43:
        print(numero, "en romanos es","XL","I"*number)
    if numero == 44:
        print(numero, "en romanos es","XLIV")

    number2 = number % 5    
    if numero >= 45 and numero <= 48:
        print(numero, "en romanos es","XLV","I"*number2)
    if numero == 49:
        print(numero, "en romanos es","XLIX")    

def romano50_59(numero):
    number = numero % 50
    if numero <= 53:
        print(numero, "en romanos es","L","I"*number)
    if numero == 54:
        print(numero, "en romanos es","LIV")

    number2 = number % 5    
    if numero >= 55 and numero <= 58:
        print(numero, "en romanos es","LV","I"*number2)
    if numero == 59:
        print(numero, "en romanos es","LIX")   

def romano60_69(numero):
    number = numero % 60
    if numero <= 63:
        print(numero, "en romanos es","LX","I"*number)
    if numero == 64:
        print(numero, "en romanos es","LXIV")

    number2 = number % 5    
    if numero >= 65 and numero <= 68:
        print(numero, "en romanos es","LXV","I"*number2)
    if numero == 69:
        print(numero, "en romanos es","LXIX")  

def romano70_79(numero):
    number = numero % 70
    if numero <= 73:
        print(numero, "en romanos es","LXX","I"*number)
    if numero == 74:
        print(numero, "en romanos es","LXXIV")

    number2 = number % 5    
    if numero >= 75 and numero <= 78:
        print(numero, "en romanos es","LXXV","I"*number2)
    if numero == 79:
        print(numero, "en romanos es","LXXIX")  

def romano80_89(numero):
    number = numero % 80
    if numero <= 83:
        print(numero, "en romanos es","LXXX","I"*number)
    if numero == 84:
        print(numero, "en romanos es","LXXXIV")

    number2 = number % 5    
    if numero >= 85 and numero <= 88:
        print(numero, "en romanos es","LXXXV","I"*number2)
    if numero == 89:
        print(numero, "en romanos es","LXXXIX")  

def romano90_99(numero):
    number = numero % 90
    if numero <= 93:
        print(numero, "en romanos es","XC","I"*number)
    if numero == 94:
        print(numero, "en romanos es","XCIV")

    number2 = number % 5    
    if numero >= 95 and numero <= 98:
        print(numero, "en romanos es","XCV","I"*number2)
    if numero == 99:
        print(numero, "en romanos es","XCIX") 

num = int(input("Ingrese un numero arábigo: "))
if num >= 1 and num <= 9:
    romano1_9(num)
if num >= 10 and num <= 19:
    romano10_19(num) 
if num >= 20 and num <= 29:
    romano20_29(num)
if num >= 30 and num <= 39:
    romano30_39(num)   
if num >= 40 and num <= 49:
    romano40_49(num)
if num >= 50 and num <= 59:
    romano50_59(num)
if num >= 60 and num <= 69:
    romano60_69(num)
if num >= 70 and num <= 79:
    romano70_79(num)      
if num >= 80 and num <= 89:
    romano80_89(num)
if num >= 90 and num <= 99:
    romano90_99(num)
if num == 100:
    print(num, "en romanos es","C") 
if num > 100:
    print("Error")       