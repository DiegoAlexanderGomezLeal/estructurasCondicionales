P1 = input("ingresa la primera palabra\n:")
P2 = input("ingresa la segunda palabra\n:")
cantidad = len(P1)-len(P2)
cantidad2 = len(P2)-len(P1)
if P1>P2:
    print(f"{P1} tiene mas caracteres que {P2}\n")
    print(f"La palabra {P1} tiene {cantidad2} letras mas que {P2}")
elif P2>P1:
    print(f"{P2} tiene mas caracteres que {P1}\n")
    print(f"La palabra {P2} tiene {cantidad} letras mas que {P1}")
else:
    print(f"{P1} tiene los mismos caracteres que {P2}\n")
    print(f"La palabra {P1} la misma cantidad de letas que {P2}")

# Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.