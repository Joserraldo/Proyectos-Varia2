Algoritmo sin_titulo
Definir contador, num, parm, imparm,x Como Entero
Escribir "***[PARES IMPARES]***"	 
Escribir "*DIGITE* [Cantidad de n�meros]"
contador = 0
leer x
Mientras contador < x Hacer
	contador = contador + 1
	Escribir "Digite un numero"
	leer num
	si num mod 2 = 0 Entonces
		parm = parm + 1	
	SiNo
		imparm = imparm + 1
	FinSi	
FinMientras
Escribir "N�meros pares: " parm 
Escribir "N�meros impares: " imparm 
FinAlgoritmo


