Algoritmo numero_mas_grande
	Escribir "****CALCULADORA DE NUMERO MAS GRANDE****"
	Escribir "Digita el número a"
	Leer a
	Escribir "Digita el número b"
	Leer b
	Escribir "Digita el número c"
	Leer c
	si a>b Entonces
		si a>c Entonces
			Escribir "a, con un valor de " a " es mayor."
		SiNo
			si a=c Entonces
				Escribir"a y c, con un valor de " a " son mayores e iguales."
			SiNo
				Escribir "c, con un valor de " c " es mayor."
			FinSi
		FinSi
	SiNo
		si c>b Entonces
			Escribir "c, con un valor de " c " es mayor."
		Sino
			Si b=c Entonces
				Si c>a Entonces
					Escribir "b y c con un valor de " b " son mayores e iguales"  
				Sino
					si a=c Entonces
						Escribir "Todos son iguales con un valor de " a
					FinSi
				FinSi
			SiNo
				si a=b entonces
					Escribir "a y b con un valor de " b " son mayores e iguales" 
				SiNo
					Escribir "b, con un valor de " b " es mayor."
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo