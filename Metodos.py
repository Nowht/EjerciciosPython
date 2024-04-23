def pie(medicion):
    print("La conversion en pulgadas: ",medicion*12)
    print("La conversion en yardas: ", round(medicion/3,3))
    print("La conversion en centimetros: ", medicion*30.48)
    print("La conversion en metros: ", round(medicion/3.281,3))

def pulgada(medicion):
    print("La conversion en pies: ", round(medicion/12,3))
    print("La conversion en yardas: ", round(medicion/36,3))
    print("La conversion en centimetros: ", medicion*2.54)
    print("La conversion en metros: ", round(medicion/39.37,3))

def yardas(medicion):
    print("La conversion en pies: ", medicion*3)
    print("La conversion en pulgadas: ", medicion*36)
    print("La conversion en centimetros: ", medicion*91.44)
    print("La conversion en metros: ", round(medicion/1.094,3))

def centimetros(medicion):
    print("La unidad de medida en pies: ",  round(medicion/30.48,3))
    print("La unidad de medida en pulgadas: ", round(medicion/2.54,3))
    print("La unidad de medida en yardas: ", round(medicion/91.44,3))
    print("La unidad de medida en metros: ", round(medicion/100,3))

def metros(medicion):
    print("La unidad de medida en pies: ", round(medicion*3.281,3))
    print("La unidad de medida en pulgadas: ", round(medicion*39.37,3))
    print("La unidad de medida en yardas: ", round(medicion*1.094,3))
    print("La unidad de medida en centimetros: ", medicion*100)

medida = int(input("Ingrese la medida: "))
unidad_medida = input("Ingrese la unidad de medida: ")

if unidad_medida == "f":    #Pies
    pie(medida)
if unidad_medida == "p":    #Pulgadas
    pulgada(medida)
if unidad_medida == "y":    #Yardas
    yardas(medida)
if unidad_medida == "c":    #Centimetros
    centimetros(medida)
if unidad_medida == "m":    #metros
    metros(medida)