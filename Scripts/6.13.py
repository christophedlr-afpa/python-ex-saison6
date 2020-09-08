nbValues: int = 0
val: int = 0
greaterVal: int = 0
values = []

nbValues = int(input("Indiquez le nombre de valeurs à rentrer : "))

for i in range(0, nbValues):
    val = int(input("Indiquez une valeur entière positive ou négative : "))
    values.append(val)

for i in range(0, nbValues):
    if i+1 <= nbValues:
        if values[i] > values[i-1]:
            greaterVal = values[i]
            pos = i

print("La plus grande valeur est : "+str(greaterVal))
print("Cette valeur est à la position : "+str(pos)+" d'un tableau de "+str(nbValues)+" valeurs")
