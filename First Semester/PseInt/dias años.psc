Algoritmo DIAS_ANOS
	Definir num, a�os, meses, dias Como enteros
	Escribir "*****CONVERTIDOR D�AS-A�OS,MESES,DIAS*****"
	Escribir "DIGITA EL N�MERO DE D�AS"
	LEER num
	a�os<-trunc(num/366)
	meses<-trunc((num mod 366 )/30)
	dias<- trunc((num mod 366 ) mod 30)
	Escribir "La cantidad de d�as digitada da como resultado: "
	si a�os=1 Entonces
		Escribir a�os " A�o."
	SiNo
		Escribir a�os " A�os."
	FinSi
	si meses=1 Entonces
		Escribir meses " Mes."
	SiNo
		Escribir meses " Meses."
	FinSi
	si dias=1 Entonces
		Escribir dias " D�a."
	SiNo
		Escribir dias " D�as."
	FinSi
FinAlgoritmo
