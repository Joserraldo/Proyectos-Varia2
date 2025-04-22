Algoritmo medidor_de_edad
	Escribir "****MEDIDOR DE EDAD****"
	Escribir "Digite su edad"
	Leer e
	si (0<=e y e<12) Entonces
		Escribir "Usted es niñ@."
	SiNo
		si (12<=e y e<18) Entonces
			Escribir "Usted es adolescente."
		SiNo
			si (18<=e y e<35) Entonces
				Escribir "Usted es adulto joven."
			SiNo
				si (35<=e y e<60) Entonces
					Escribir "Usted es Adulto"
				SiNo
					si (60<=e ) Entonces
						Escribir "Usted es Adulto mayor"
					SiNo
						Escribir "ERROR"
					FinSi
				FinSi
			FinSi
		FinSi
		
	FinSi

FinAlgoritmo
