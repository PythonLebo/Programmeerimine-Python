def keskmised(mArray):
    for aine in mArray:
        temp = 0
        for hinne in aine[1:]:
            temp = temp + int(hinne)
        print(f"{aine[0]}: {round(temp/(len(aine)-1),1)}")

file = open("hinded.csv", encoding="UTF-8")
matrix = []
for rida in file:
    row = []
    array = rida.split(",")

    for i in array:
        row.append(i)

    matrix.append(row)

file.close()

keskmised(matrix)

#####################################################################

import csv
hinded = []
with open("hinded.csv") as fail:
    csvr = csv.reader(fail, delimiter=',')
    for rida in csvr:
        osad = []
        osad.append(rida[0])
        del rida[0]
        for osa in rida:
            osad.append(int(osa))
        hinded.append(osad)

def keskmised(i):
    e = []
    for a in i:
        e1 = []
        w0 = 0
        for w in a:
            if type(w) == type('str'):
                e1.append(w)
            else:
                w0 += w
        ind = len(a) - 1
        e1.append(round(w0 / ind, 1))
        e.append(e1)
    return e
kesk = keskmised(hinded)
for u in kesk:
    aine = u[0]
    hinne = u[1]
    print("{}: {}".format(aine, hinne))
