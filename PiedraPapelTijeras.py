while True: 
    j1 = (input("Jugador 1: "))
    j2 = (input("Jugador 2: "))

    if (j1 == "piedra" and j2 == "tijera") or (j1 == "tijera" and j2 == "papel") or (j1 == "papel" and j2 == "piedra"):
        print("El jugador 1 gana")
    if (j2 == "piedra" and j1 == "tijera") or (j2 == "tijera" and j1 == "papel") or (j2 == "papel" and j1 == "piedra"):
        print("El jugador 2 gana")
    if j1 == j2:
        print("empate") 
        
    x = input("desea jugar otra vez? s/n: ")
    if x == "n":
        break    