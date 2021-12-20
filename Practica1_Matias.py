print("\n\t\t==> Bienvenido Tripulante <==\t\t\n")

cadena1   = input("Enter room: ")
caracter = cadena1[0:2]
caracter2 = cadena1[-3:]
caracter3 = str(caracter) + str(caracter2)
print(f"\nEsta es tu cadena con las primeras 2 y las ultimas 3 = {caracter3}\n")
print(f"\nLa cadena por cada  caracter es = {cadena1 * len(cadena1)}\n")