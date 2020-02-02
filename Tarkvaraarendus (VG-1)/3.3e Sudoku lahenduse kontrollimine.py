def kastid_korras(maatriks):
    # Vaatame igat 3x3 kasti
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            # Iga kasti korral kogume tema elemendid järjendisse 'kast'
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
            # Ja kontrollime, kas elemendid on korrektsed
            if sorted(kast) != list(range(1, 10)):
                return False
    return True

def row_check(t):
    for i in t:
        if sorted(i) != list(range(1, 10)):
            return False
    return True

def column_check(t):
    for x in range(9):
        temp = []
        for i in t:
            temp.append(i[x])
        if sorted(temp) != list(range(1, 10)):
            return False
    return True


fail = open(str(input()), encoding="UTF-8")

matrix = []

for rida in fail:
    row = []
    array = rida.split()

    for num in array:
        row.append(int(num))

    matrix.append(row)

fail.close()

if kastid_korras(matrix) and row_check(matrix) and column_check(matrix):
    print("OK")
else:
    print("VIGA")
    
################################################################################################

failn = input("Sisestage faili nimi: ")
laud = []
with open(failn, encoding="UTF-8") as fail:
    for rida in fail:
        ew = []
        osad = rida.split()
        for osa in osad:
            ew.append(int(osa))
        laud.append(ew)
            

def kastid_korras(maatriks):
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
            if sorted(kast) != list(range(1, 10)):
                return False
    return True

def read_korras(maatriks):
    for a in maatriks:
        if sorted(a) != list(range(1, 10)):
            return False
    return True

def veerud_korras(maatriks):
    a = zip(*maatriks)
    for i in a:
        q = []
        q.append(i)
        for x in q:
            if sorted(x) != list(range(1, 10)):
                return False
    return True

def sudoku_korras(maatriks):
    if (kastid_korras(maatriks) == True
    and read_korras(maatriks) == True
    and veerud_korras(maatriks) == True):
        return print("OK")
    return print("VIGA")

sudoku_korras(laud)
