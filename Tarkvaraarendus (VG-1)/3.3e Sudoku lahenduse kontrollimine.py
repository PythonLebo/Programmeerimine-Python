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