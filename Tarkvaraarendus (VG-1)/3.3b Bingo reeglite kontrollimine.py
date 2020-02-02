def on_bingo_tabel(matrix):
    for x in matrix:
        last = 0
        for v in x:
            if not (v in range(last,last+16)):
                return False
            last = last + 15
    return True

########################################################

def on_bingo_tabel(i):
    for a in i:
        if a[0] in range(1, 16) and a[1] in range(16, 31) and a[2] in range(31, 46) and a[3] in range(46, 61) and a[4] in range(61, 76):
            e = True
        else:
            e = False
        if e == False:
            return False
    return True
