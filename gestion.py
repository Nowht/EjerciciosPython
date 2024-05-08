class Administrador:
    saldo = 0
    resta = 0
    def __init__(self, dinero):
        self.dinero = dinero

    def ingreso(self):
        Administrador.saldo += self.dinero

    def gasto(self):
        Administrador.resta += self.dinero

    def balance(self):
        return Administrador.saldo - Administrador.resta

    def registro(self):
        print(f"Registros\nEntrada: {Administrador.saldo} | Salida: {Administrador.resta}")

while True:
    print("\n1. Agregar ingreso\
           \n2. Agregar gasto\
           \n3. Ver balance\
           \n4. Ver registros\
           \n5. Salir")
    opcion = int(input("\nIngrese una opción: "))
    print("") 

    if opcion == 1:
        ingreso = float(input("Agregue ingreso: "))
        gestion = Administrador(ingreso)
        gestion.ingreso()

    if opcion == 2:
        gasto = float(input("Agregue gastos: "))
        gestion = Administrador(gasto)
        gestion.gasto()

    if opcion == 3:
        gestion = Administrador(0)
        print(f"Balance: {gestion.balance()}")
    
    if opcion == 4:
        gestion = Administrador(0)
        gestion.registro()
    
    if opcion == 5:
        break

