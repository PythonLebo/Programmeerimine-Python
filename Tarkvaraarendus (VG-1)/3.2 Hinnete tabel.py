def keskmised(mArray):
    newArray = []
    for aine in mArray:
        temp = 0
        for hinne in aine[1:]:
            temp = temp + hinne
        newArray.append([aine[0],round(temp/(len(aine)-1),1)])
    return newArray

###########################################################################

def keskmised(i):
    e = []
    for a in i:
        e1 = []
        w0 = 0
        q = 0
        for w in a:
            if type(w) == type('str'):
                e1.append(w)
            else:
                w0 += w
        ind = len(a) - 1
        e1.append(round(w0 / ind, 1))
        e.append(e1)
    return e
