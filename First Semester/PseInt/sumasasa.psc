Algoritmo sin_titulo
	Definir contador, num, digito Como Entero
	Escribir "[***SUMA DE NUMEROS EN SECUENCIA***]"
	Escribir "¿Hasta que número desea sumar?"
	leer x
	Escribir "DIGITE [1. suma todos] [2. suma pares] [3. suma impares]"
	leer digito
	mientras contador <= x Hacer
		contador = contador +1
		Si digito = 1 Entonces
			suma = suma + num
			num = num+1
		SiNo 
			si digito = 2 Entonces
				Si num mod 2 = 0
					suma = suma + num
				FinSi	
				num = num+1
			Sino 
				si digito = 3 Entonces
					Si num mod 2 = 1
						suma = suma + num
					FinSi	
					num = num+1
				FinSi
			Finsi
		FinSi
	FinMientras
	Escribir "El resultado de la suma es: " suma
FinAlgoritmo


