Algoritmo CALCULADORA_MODOS
	Escribir "*****MULTIPLOS DEL NUMERO*****"
	definir contador,cant, mult, max como entero
	Escribir "¿Que multipos desea saber?"
	Leer mult
	Escribir "¿Hasta que número desea saber?"
	leer max
	contador<-1
	cant<-0
	Escribir "los multiplos de " mult " hasta el" max "son"
	Mientras contador <= max hacer
		si (contador mod mult) = 0 Entonces
			cant <- cant+1
			Escribir contador
		FinSi
		contador <- contador+1
	FinMientras
	Escribir "la cantidad de multiplos de " mult " es: " cant 
FinAlgoritmo 