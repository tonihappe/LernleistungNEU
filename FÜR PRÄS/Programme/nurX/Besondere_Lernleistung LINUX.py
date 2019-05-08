import math

def getBeschl(PR):
	mM = 7.349e22				#in kg
	mE = 5.972e24				#in kg
	mR = 5000					#in kg
	G = 6.67408e-11				#in m^3/s^2kg; Gravitationskonstante
	rEM = 3844e5				#in m; Abstand Erde-Mond

	#Berechnung der Kraefte und der Beschleunigung
	FE =-1*G*mR*mE/(PR**2)		#Gravitationskraft Erde, N
	FM = G*mR*mM/((rEM-PR)**2)	#Gravitationskraft Mond, N
	FRES = FE+FM				#resultierende Kraft, N
	aR = (FRES/mR)				#resultierende Beschleunigung, m/s^2

	return aR, FRES,FE,FM


#Deklarationen
n= 1000000			#Anzahl an maximalen Wiederholungen
h = 1				#Schrittweite

t=[0]*n				#Zeit, s
PR=[0]*n			#Position des Raumschiffes, m (Entfernung vom Erdmittelpunkt)
v=[0]*n				#Geschwindigkeit des Raumschiffes, m/s

rM = 1737e3			#Mondradius, m
rE = 6371e3			#Erdradius, m
rEM = 3844e5		#Abstand Erde-Mond, m

#Anfangswerte
t[0]=0			#Anfang der "Zeitzaehlung" auf 0 setzen
PR[0]=6371e3	#Startposition des Raumschiffs (Auf Erdoberflaeche --> Radius der Erde)

#Eingabe der Startgeschwindigkeit
print("Startgeschwindigkeit (Punkt als Dezimaltrennzeichen): ")
v[0]=float(input())
print("\n\n")

#Berechnungen fuer die Anfangswerte
aR, FRES,FE,FM = getBeschl(PR[0]) #Erster Aufruf des Unterprogramms "getbeschl"
ausg = open ("Ausgabe.dat","w")
ausg.write(str(t[0])+"\t"+str(PR[0])+"\t"+str(v[0])+"\t"+str(aR)+"\t"+str(FRES)+"\t"+str(FE)+"\t"+str(FM)+"\n") #Ergebnisse des ersten Aufrufs in die Datei schreiben

#Schleife fuer einzelne Berechnung am jeweiligen Punkt
for i in range(1,n,1):
	aR, FRES,FE,FM =getBeschl(PR[i-1])
	#print("FRES = ", FRES,"\naR = ",aR)

	#RungeKutta4

	#k berechnet PR
	#l berechnet v

	k1 = v[i-1]
	l1 = aR

	k2 = v[i-1]+0.5*h*l1
	l2 = aR

	k3 = v[i-1]+0.5*h*l2
	l3 = aR

	k4 = v[i-1]+ h * l3
	l4 = aR

	PR[i] = PR[i-1]+ h/6.0 * (k1 + 2 * k2 + 2* k3 + k4) #Berechnen der neuen Position
	v[i]  = v[i-1] + h/6.0 * (l1 + 2 * l2 + 2* l3 + l4) #Berechnen der neuen Geschwindigkeit
	t[i] = t[i-1]+h

	#print("DURCHGANG NUMMER: ", i)
	#Test ob Raumschiff Mond oder Erde erreicht hat
	if (PR[i]<=rE):
		print("\n\n\n\n\nAuf Erde aufgeschlagen!\n\n")
		print("Verstrichene  Durchgaenge: "+str(i)+"\n")
		ausg.close()
		abbruch=bool(True)
		break

	elif(PR[i]>(rEM-rM)):
		print("\n\n\n\n\nAuf Mond aufgeschlagen!\n\n")
		print("Verstrichene  Durchgaenge: "+str(i)+"\n")
		ausg.close()
		abbruch=bool(True)
		break

	#werte in datei
	ausg.write(str(t[i])+"\t"+str(PR[i])+"\t"+str(v[i])+"\t"+str(aR)+"\t"+str(FRES)+"\t"+str(FE)+"\t"+str(FM)+"\n")

if (abbruch==False):
	print("\n\n\n\n\nMaximale Anzahl an Durchgaengen ueberschritten! (>1000000)")
	ausg.close()
