caracter = input("ingrese caracter\n:")

if caracter.isalpha():
    if caracter.isupper():
        print("este caracter es una letra mayuscula\n") 
    elif caracter.islower():
        print("este caracter es una letra minuscula\n")
else:
    if caracter.isdigit():
        print("este caracter es un numero\n:")
    else:
        print("INGRESE UN CARACTER VALIDO")

# Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.