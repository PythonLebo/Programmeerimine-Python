import csv
all, biggest, name = 0, 0, str
with open("maalähedane.csv") as fail:
    for rida in csv.reader(fail, delimiter=";"):
        temp = sum(map(int, rida[1:]))
        all += temp
        if temp > biggest:
            biggest, name = temp, rida[0]
print(f'Kõige rohkem osalejaid - {name}, {biggest} inimest.\nKokku on kursusel osalenud {all} inimest')
#######################################################################################################
import csv
ml = []
with open("maalähedane.csv", encoding="UTF-8") as fail:
    csvr = csv.reader(fail, delimiter=';')
    for rida in csvr:
        ew = []
        ew.append(rida[0])
        del rida[0]
        for osa in rida:
            ew.append(int(osa))
        ml.append(ew)
suurim = []
kokku = 0
for a in ml:
    kokku += sum(a[1:])
    if sum(a[1:]) > sum(suurim[1:]):
        suurim = a
print("Kõige rohkem osalejaid - {}, {} inimest.".format(suurim[0], sum(suurim[1:])))
print("Kokku on kursusel osalenud {} inimest.".format(kokku))
