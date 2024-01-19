L1=float(input("Ingrese lado 'a' del triangulo: "))
L2=float(input("Ingrese lado 'b' del triangulo: "))
L3=float(input("Ingrese lado 'c' del triangulo: "))
rev1=L1+L2
rev2=L1+L3
rev3=L2+L3
if rev1<L3:
    print("No es un triangulo valido")
elif rev2<L2:
    print("No es un triangulo válido")
elif rev3<L1:
    print("No es un triangulo valido")
else:
    if L1==L2==L3:
        print("Es un triangulo equilatero")
    elif L1==L2 or L2==L3 or L1==L3:
        print("Es un triangulo isósceles")
    else:
        print("Es un triangulo escaleno")