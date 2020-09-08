val: int
temp: int
pos: int = 0
arraySort = []
changed: bool = False

for i in range(0, 100):
    val = int(input("Indiquez un nombre pour la position "+str(i)+" : "))
    arraySort.append(val)

    for x in range(0, len(arraySort)):
        for j in range(x, len(arraySort)):
            if arraySort[j] < arraySort[x]:
                pos = j
                changed = True

        if changed:
            temp = arraySort[pos]
            arraySort[pos] = arraySort[x]
            arraySort[x] = temp
            changed = False

print("Liste des valeurs :")

for i in arraySort:
    print(i)
