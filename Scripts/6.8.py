nbrValues: int = 0
nbrNegative: int = 0
nbrPositive: int = 0
nbrZzero: int = 0
val: int = 0
values = []

nbrValues = int(input("Indiquez le nombre de valeurs que vous désirez entrer : "))

for i in range(0, nbrValues):
    val = int(input("Donnez une valeur numérique entière positive ou négative : "))

    if val < 0:
        nbrNegative += 1
    elif val > 0:
        nbrPositive += 1
    else:
        nbrZzero += 1

    values.append(val)

print("Vous avez rentré "+str(nbrValues)+" valeurs au total, dont :")
print("- "+str(nbrNegative)+" valeurs négatives")
print("- "+str(nbrPositive)+" valeurs positives")
print("- "+str(nbrZzero)+" valeurs à zéro")
