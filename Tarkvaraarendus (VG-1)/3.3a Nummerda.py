def nummerda(r1,r2):
    array = []
    for korrus in range(1,r1+1):
        temp = []
        for korter in range(1,r2+1):
            temp.append(str(korrus) + str(korter))
        array.append(temp)
    return array

#########################################################

def nummerda(i , o):
    e = []
    for a in range(i):
        e1 = []
        for b in range(o):
            e1.append(str(a + 1) + str(b + 1))
        e.append(e1)
    return e
