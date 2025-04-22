Algoritmo sin_titulo
Definir contador, num, parm, imparm,x Como Entero
Escribir "***[PARES IMPARES]***"	 
Escribir "*DIGITE* [Cantidad de números]"
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
Escribir "Números pares: " parm 
Escribir "Números impares: " imparm 
FinAlgoritmo


