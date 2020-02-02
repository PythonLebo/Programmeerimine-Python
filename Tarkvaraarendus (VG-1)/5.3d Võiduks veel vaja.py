#Nurkademäng
def nurkademanguks_vaja(i):
    puudu = []
    if type(i[0][0]) == type(0):
        puudu.append(i[0][0])
    if type(i[0][4]) == type(0):
        puudu.append(i[0][4])
    if type(i[4][0]) == type(0):
        puudu.append(i[4][0])
    if type(i[4][4]) == type(0):
        puudu.append(i[4][4])
    return puudu

#Peadiagonaal
  
def x_peadiagonaalil(i):
    l = 0
    f = 0
    b = []
    for a in i:
        if a[l] == "X":
            f += 1
        else:
            b.append(a[l])
        l += 1
    return b
#Kõrvaldiagonaal

def x_korvaldiagonaalil(i):
    l = 4
    f = 0
    b = []
    for a in i:
        if a[l] == "X":
            f += 1
        else:
            if l != 2:
                b.append(a[l])
        l -= 1
    return b
#Diagonaalidemäng

def diagonaalidemanguks_vaja(i):
    o = []
    for a in x_peadiagonaalil(i):
        o.append(a)
    for u in x_korvaldiagonaalil(i):
        o.append(u)
    return o

#Täismäng

def taismanguks_vaja(i):
    o = []
    for a in i:
        for u in a:
            if u != 'X':
                o.append(u)
    return o
