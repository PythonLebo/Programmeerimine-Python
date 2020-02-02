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
