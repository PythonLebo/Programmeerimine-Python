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
