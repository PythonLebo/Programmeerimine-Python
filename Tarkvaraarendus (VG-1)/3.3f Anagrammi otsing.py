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