N1 = float(input("ingrese el primer digito\n:"))
N2 = float(input("ingrese el segundo digito\n:"))
print("elegir la operacion deseada\n:")
operacion = input("\t1. Suma\n\t2. Resta\n\t3. Multiplicacion\n\t4. Division\n:")

if operacion == "1":
    op1 = N1+N2
    print("el resultado es", op1)
elif operacion == "2":
    op2 = N1-N2
    print("el resultado es", op2)
elif operacion == "3":
    op3 = N1*N2
    print("el resultado es", op3)
elif operacion == "4":
    op4 = N1/N2
    print("el resultado es", op4)
else:
    print("caracteres no validos")

# Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.