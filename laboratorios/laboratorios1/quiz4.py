x = True
frase=0
agua=0
fuego=0
agre = []

print("hola")

while x :

        frase = input("digite una frase ")
        if "agua" in frase:
            agua=agua+1

        if "fuego" in frase:
            fuego=fuego+1
        if "agua" in frase or "fuego" in frase:
            agre.append(frase)
        if frase == "salir":
            x = False
print("cantidad de agua: " ,agua)
print("cantidad de fuego: " ,fuego)
print (agre)
