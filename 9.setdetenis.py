a = int(input("Ingrese puntaje de A:\n"))
b = int(input("Ingrese puntaje de B:\n"))

if (a == 4 and b == 5):
    print("Continua")
elif (a >= 4 and b == 7):
    print("Gana B")
elif (a == 5 and b == 6):
    print("Continua")
elif (a == 3 and b == 7):
    print("Invalido")
elif (a <= 6 and b <= 4):
    print("Gana A")