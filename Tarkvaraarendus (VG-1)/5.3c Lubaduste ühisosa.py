def kooslubajad(i):
    t = 100
    r = 0
    for a in i:
        for u in range(len(i)):
            if i.index(a) != u:
                if len(a.difference(i[u])) < t and len(a.difference(i[u])) != 0:
                    t = len(a.difference(i[u]))
                    r = (i.index(a), u)
    return r
