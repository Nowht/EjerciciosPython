
num = int(input("ingrese numero"))
dig1= num // 10000000
dig2= num % 10000000
dig2= dig2 // 1000000
dig3= num % 1000000
dig3= dig3 // 100000
dig4= num % 100000
dig4= dig4 // 10000
dig5= num % 10000
dig5= dig5 // 1000
dig6= num % 10000
dig6= dig6 // 1000
dig7= num % 1000
dig7= dig7 // 100
dig8= num % 10
dig8= dig8 // 10

print(dig8)
