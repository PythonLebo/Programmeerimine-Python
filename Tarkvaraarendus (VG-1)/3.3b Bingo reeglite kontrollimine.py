def on_bingo_tabel(matrix):
    for x in matrix:
        last = 0
        for v in x:
            if not (v in range(last,last+16)):
                return False
            last = last + 15
    return True