def failist_sonastik(i):
    e = {}
    with open(i, encoding="UTF-8") as fail:
        for rida in fail:
            osa = rida.split()
            e[osa[0]] = osa[1]
    return e

def tahised_nimedeks(i, a):
    w = []
    for q in i:
        if q in a:
            w.append(a[q])
        else:
            w.append(None)
    return w
failn = input("Sisestage andmebaasi faili nimi: ")
piir = input("Piiriületajad: ").split()
nimed = tahised_nimedeks(piir, failist_sonastik(failn))
for u in nimed:
    if u == None:
        print("Tundmatu maa")
    else:
        print(u)
