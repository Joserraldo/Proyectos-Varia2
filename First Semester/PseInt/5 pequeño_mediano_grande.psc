Algoritmo peque�o_mediano_grande
	Escribir "****CALCULADORA N�MERO PEQUE�O, MEDIANO Y GRANDE****"
	Escribir "RECUERDE: NO SE ACEPTAN NUMEROS IGUALES"
	Escribir "Digita el n�mero a"
	Leer a
	Escribir "Digita el n�mero b"
	Leer b
	Escribir "Digita el n�mero c"
	Leer c
	Si (a=b o b=c o a=c) Entonces
		Escribir "ERROR (NO SE ACEPTAN N�MEROS IGUALES)"
	SiNo
		si a>b Entonces
			si a>c Entonces
				si b>c Entonces
					Escribir "a es el mayor con un valor de " a ", b es el mediano con un valor de " b " y c es el menor con un valor de " c
				SiNo
					Escribir "a es el mayor con un valor de " a ", b es el menor con un valor de " b " y c es el mediano con un valor de " c
				FinSi
			SiNo
				Escribir "a es el mediano con un valor de " a ", b es el menor con un valor de " b " y c es el mayor con un valor de " c	
			FinSi
		SiNo
			si b>c Entonces
				si a>c Entonces
					Escribir "a es el mediano con un valor de " a ", b es el mayor con un valor de " b " y c es el menor con un valor de " c
				SiNo
					Escribir "a es el menor con un valor de " a ", b es el mayor con un valor de " b " y c es el mediano con un valor de " c
				FinSi
			SiNo
				Escribir "a es el menor con un valor de " a ", b es el mediano con un valor de " b " y c es el mayor con un valor de " c
			FinSi
		FinSi
	FinSi
FinAlgoritmo
