import math
from collections import defaultdict
def sorteeri(string):
    ret = defaultdict(list)
    with open(string) as file:
        for rida in file.read().splitlines():
            array = rida.split(";")
            ret[math.floor(int(array[2])*0.1)*10].append(array)
    return ret

def kuva(dict):
    for y in sorted(dict):
        val,biggest,arr = dict[y],0,list 
        for a in val:
            if int(a[3]) > biggest:
                biggest,arr = int(a[3]),a
        print(f'{y}: {len(val)} album(it) ({arr[0]} - {arr[1]})')
kuva(sorteeri("albumid.txt"))
#################################################################
def sorteeri(q):
    e = {}
    with open(q, encoding="UTF-8") as fail:
        for rida in fail:
            row = rida.strip()
            row = row.split(";")
            voti = int(row[2][:-1] + '0')
            if voti in e:
                x = e.get(voti)
                x += [row]
                e[voti] = x
            else:
                e[voti]= [row]
    p = {}
    for key in sorted(e.keys()):
        p[key] = e[key]
    return(p)

def kuva(i):
    for w in i.items():
        suurim = w[1:][0][0]
        for o in w[1:]:
            for u in o:
                if int(suurim[3]) < int(u[3]):
                    suurim = u
        print("{}: {} album(it) ({} - {})".format(w[0], len(w[1]), suurim[0] , suurim[1]))
kuva(sorteeri("albumid.txt"))
