hora=int(input("Ingrese la hora: "))
minutos=int(input("Ingrese el minuto: "))
duracion=int(input("Ingrese la duracion del evento: "))

min_totales=minutos+duracion
hora_totales=hora+min_totales//60
min_totales = min_totales%60
hora_totales = hora_totales%24

print("la hora de finzalizar sera: ", hora_totales,":",min_totales)