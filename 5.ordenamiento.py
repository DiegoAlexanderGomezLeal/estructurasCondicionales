N1 = int(input("ingresa el primer numero"))
N2 = int(input("ingresa el swegundo numero"))
if N1<N2:
    print(f"{N1} {N2}")
else:
    print(f"{N2} {N1}")
# primer programa para 2 numeros


N1 = int(input("ingresa el primer numero\n:"))
N2 = int(input("ingresa el segundo numero\n:"))
N3 = int(input("ingresa el tercer numero\n:"))

if N1>N2 and N1>N3 and N2>N3:
    print(f"{N3} {N2} {N1}")

elif N1>N2 and N1>N3 and N3>N2:
    print(f"{N2} {N3} {N1}")

elif N2>N1 and N2>N3 and N1>N3:
    print(f"{N3} {N1} {N2}")

elif N2>N1 and N2>N3 and N3>N1:
    print(f"{N1} {N3} {N2}")

elif N3>N2 and N3>N1 and N2>N1:
    print(f"{N1} {N2} {N3}")

elif N3>N2 and N3>N1 and N1>N2:
    print(f"{N2} {N1} {N3}")
else:
    print("ingrese numeros enteros")
# segundo programa para 3 numeros

N1 = int(input("ingresa el primer numero\n:"))
N2 = int(input("ingresa el segundo numero\n:"))
N3 = int(input("ingresa el tercer numero\n:"))
N4 = int(input("ingresa el cuarto numero\n:"))
numeros = [N1, N2, N3, N4]
numeros.sort()
if numeros:
    print(numeros)
else:
    print("ingrese numeros enteros")
# tercer programa para 4 numeros