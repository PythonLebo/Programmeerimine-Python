def symbolite_sagedus(i):
    e = {}
    for char in i:
        e[char] = e.setdefault(char, 0) + 1
    return e
