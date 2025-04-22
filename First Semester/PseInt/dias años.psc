Algoritmo DIAS_ANOS
	Definir num, años, meses, dias Como enteros
	Escribir "*****CONVERTIDOR DÍAS-AÑOS,MESES,DIAS*****"
	Escribir "DIGITA EL NÚMERO DE DÍAS"
	LEER num
	años<-trunc(num/366)
	meses<-trunc((num mod 366 )/30)
	dias<- trunc((num mod 366 ) mod 30)
	Escribir "La cantidad de dÍas digitada da como resultado: "
	si años=1 Entonces
		Escribir años " Año."
	SiNo
		Escribir años " Años."
	FinSi
	si meses=1 Entonces
		Escribir meses " Mes."
	SiNo
		Escribir meses " Meses."
	FinSi
	si dias=1 Entonces
		Escribir dias " Día."
	SiNo
		Escribir dias " Días."
	FinSi
FinAlgoritmo
