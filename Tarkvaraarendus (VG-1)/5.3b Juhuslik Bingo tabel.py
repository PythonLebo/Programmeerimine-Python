def juhuslik_bingo():
    from random import sample
    e = []
    for a in range(5):
        arvud = sample(range(a*15+1, a*15+16), 5)
        e.append(arvud)
    tabel = zip(*e)
    o = []
    for u in tabel:
        i = []
        for w in u:
            i.append(w)
        o.append(i)
    return o
