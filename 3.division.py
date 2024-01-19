Dividendo = int(input("ingrese el numero dividendo\n:"))
Divisor = int(input("ingrese el numero divisor\n:"))
operacion =  (Dividendo/Divisor)
residuo = Dividendo%Divisor
cociente = Dividendo//Divisor

if operacion != 0:
    print("su operacion es exacta\n")
    print(f"el resultado de su operacion es\n:{operacion}\n")
    print(f"restante\n:{residuo}\n")
    print(f"cociente\n{cociente}\n")

elif operacion == 0:
    print("su operacion no es exacta\n")
    print(f"el resultado de su operacion es\n:{operacion}\n")
    print(f"restante\n:{residuo}\n")
    print(f"cociente\n{cociente}\n")


# Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
    