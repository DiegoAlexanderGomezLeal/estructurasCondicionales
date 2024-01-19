año = 0
mes = 0
dia = 0
while año==0 and mes==0 and dia==0: 
    año=int(input("Ingrese su año de nacimiento:\n"))
    mes=int(input("Ingrese su mes de nacimiento:\n"))
    dia=int(input("Ingrese su dia de nacimiento:\n"))
    if año>=9999 or año<0 or mes>=12 or mes<=0 or dia>=31:
        print("---Ingrese correctamente los datos. ¡Vuelva a intentarlo!---")
        año=0
        mes=0
        dia=0
    else:
        from time import localtime
        t=localtime() 
        difaño=t.tm_year-año
        difmes=t.tm_mon-mes
        difdia=t.tm_mday-dia
        if difmes==0:
            if difdia<0:
                print(f"Usted tiene {difaño-1} años.")
            else:
                print(f"Usted tiene {difaño} años.")
        elif difmes>0:
            print(f"Usted tiene {difaño} años.")
        else:
            print(f"Usted tiene {difaño-1} años.")