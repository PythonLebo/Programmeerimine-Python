file = open(str(input()), encoding="UTF-8")
biggest = False
ridaB = NotImplemented
for i,rida in enumerate(file):
    array = rida.split()
    temp = int(array[0])

    for num in array[1:]:
        temp = temp + int(num)

    if not biggest or temp > biggest:
        biggest = temp
        ridaB = i + 1

file.close()

print("Suurim summa on failis {}. real ja see on {}.".format(ridaB,biggest))

#######################################################################################

failn = input("Sisestage failinimi: ")
arvud = []
with open(failn, encoding="UTF-8") as fail:
    for rida in fail:
        summa = 0
        osad = rida.split()
        for osa in osad:
            summa += int(osa)   
        arvud.append(summa)
print("Suurim summa on failis {}. real ja see on {}.".format(arvud.index(max(arvud)) + 1, max(arvud)))
