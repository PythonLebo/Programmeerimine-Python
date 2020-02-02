def paarissumma(i):
    if i % 2 != 0:
        i -= 1
    if i == 0:
        return 0
    else:
        return i + paarissumma(i-2)
