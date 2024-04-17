registro = {"Nombre":"","Edad":"","Direccion":"","Telefono":""}

for i in registro:
    ingresado = input(f"Ingrese su {i}: ")
    registro[i]=ingresado

print("")
print(f"{registro.get("Nombre")} tiene {registro.get("Edad")} años, vive en {registro.get("Direccion")} y su numero de telefono es {registro.get("Telefono")}\n")