Algoritmo CompararLongitudesPalabras
    Definir P1, P2 Como Caracter
    Definir cantidad, cantidad2 Como Entero
	
    Escribir "Ingresa la primera palabra:"
    Leer P1
    Escribir "Ingresa la segunda palabra:"
    Leer P2
	
    cantidad = Longitud(P1) - Longitud(P2)
    cantidad2 = Longitud(P2) - Longitud(P1)
	
    Si P1 > P2 Entonces
        Escribir P1, " tiene más caracteres que ", P2
        Escribir "La palabra ", P1, " tiene ", Abs(cantidad2), " letras más que ", P2
    Sino
        Si P2 > P1 Entonces
            Escribir P2, " tiene más caracteres que ", P1
            Escribir "La palabra ", P2, " tiene ", Abs(cantidad), " letras más que ", P1
        Sino
            Escribir P1, " tiene la misma cantidad de caracteres que ", P2
            Escribir "Las palabras ", P1, " y ", P2, " tienen la misma cantidad de letras"
        FinSi
    FinSi
FinAlgoritmo

