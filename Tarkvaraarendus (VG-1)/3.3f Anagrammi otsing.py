def val(char):
    return sum(bytearray(char,"UTF-8"))

def leidub_anagramm(t):
    for i in t:
        for k,v in enumerate(i):
            if len(i) == 1:
                if val(v) == 0:
                    return True
            else:
                if k == 0:
                    if val(v) == val(i[k+1]):
                        return True
                elif k == len(i)-1:
                    if val(v) == val(i[k-1]):
                        return True
                elif val(v) == val(i[k-1]) + val(i[k+1]):
                    return True
    return False


print(leidub_anagramm([['cad'], ['a', 'bad', 'bd']]))

##############################################################################

def leidub_anagramm(i):
    for a in i:
        if len(a) == 1:
            if a[0] == '':
                return True
            return False
        e = []
        for u in a[0]:
            e.append(u)
        if len(a) == 3:
            for y in a[2]:
                e.append(y)
            if len(a[2]) > len(a[1]):
                return False
        r = 0
        for t in e:
            if t in a[1]:
                r += 1
        if r >= len(a[1]):
            if len(a[0]) > len(a[1]):
                return False
        else:
            return False
    return True
