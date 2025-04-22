Algoritmo BIN_DEC_DEC_BIN
	Definir func,n,x,binari0, decimal como entero
	Definir binario Como Caracter
	Escribir "*****CONVERTIDOR BINARIO-DECIMAL Y DECIMAL-BINARIO*****"
	Escribir "Digite 1 para convertir BINARIO-DECIMAL, 2 para DECIMAL-BINARIO y 0 para SALIR"
	leer func
	si func = 1 o func = 2 o func = 0 
		Mientras func >= 1 hacer
			si func=1 Entonces
				Escribir "Digite el número para convertir BINARIO-DECIMAL"
				leer n
				binario <- ConvertirATexto(n)
				n<- longitud (binario)
				x<-0
				decimal <- 0
				mientras n > 0 Hacer
					Si SubCadena(binario,n,n) = "1" Entonces
						decimal = decimal + 2^x
					FinSi
					n<- n - 1
					x<- x + 1
				FinMientras
				Escribir decimal 
				Escribir "¿Desea continuar? Digite 1 para convertir BINARIO-DECIMAL, 2 para DECIMAL-BINARIO y 0 para SALIR"
				leer func
			Sino 
				Escribir "Digite el número para convertir DECIMAL-BINARIO"
				leer n
				x <- 1
				mientras n >= 1
					si n mod 2 = 1 entonces 
						binari0 <- binari0 + x
					FinSi
					x <- x * 10
					n <- trunc(n/2)
				FinMientras
				escribir binari0
				Escribir "¿Desea continuar? Digite 1 para convertir BINARIO-DECIMAL, 2 para DECIMAL-BINARIO y 0 para SALIR"
				leer func
			FinSi
		FinMientras
		Escribir "Fin, gracias " 
	Sino 
		Escribir "Error"
	FinSI
	
FinAlgoritmo 