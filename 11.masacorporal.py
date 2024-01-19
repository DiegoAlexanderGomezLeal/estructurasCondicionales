altura = float(input("ingrese su estatura en centimetros"))
edad = float(input("ingrese su edad"))
peso = float(input("ingrese su peso en kilogramos"))
IMC = peso/(altura*altura)
if edad<45:
    if IMC < 22:
        print("el riesgo de que usted sufra riesgos es bajo")

    elif IMC >= 22:
        print("el riesgo de que usted sufra riesgos es medio")

elif edad>=45:
    if IMC < 22:
        print("el riesgo de que usted sufra riesgos es medio")

    elif IMC >= 22:
        print("el riesgo de que usted sufra riesgos es alto")

else:
    print("ingrese medidas como se espesifico")
# IMC < 22.0	bajo	medio
# Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.