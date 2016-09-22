cen = float(input("introduzca la cantidad de moneda:"))

eur = 0.8965
yen = 101.5744
bp = 0.7702
mxn = 197843

dol = (cen/100)
a = dol*eur
b = dol*yen
c = dol*bp
d = dol*mxn

print ("convertir a ero:" + str(a))
print ("convertir a yen:" + str(b))
print ("convertit a bp" + str(c))
print ("convertir a mxn:" + str(d))
