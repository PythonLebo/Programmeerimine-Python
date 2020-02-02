def voitis_nurkademangu(t):
    if t[0][0] == "X" and t[0][4] == "X" and t[4][0] == "X" and t[4][4] == "X":
        return True
    else:
        return False

def x_peadiagonaalil(t):
    x_arv = 0
    for i in range(5):
        if t[i][i] == "X":
            x_arv = x_arv + 1
    return x_arv

def x_korvaldiagonaalil(t):
    x_arv = 0
    for i in range(5):
        if t[i][4-i] == "X":
            x_arv = x_arv + 1
    return x_arv

def voitis_diagonaalidemangu(t):
    if x_korvaldiagonaalil(t) == 5 and x_peadiagonaalil(t) == 5:
        return True
    else:
        return False

def voitis_taismangu(t):
    for i in t:
        for v in i:
            if v != "X":
                return False

    return True

#####################################################################################

#Nurkademäng

def voitis_nurkademangu(i):
    l = 0
    f = 0
    for a in i:
        if l == 0:
            if a[0] == "X" and a[4] == "X":
                f += 1
        if l == 4:
            if a[0] == "X" and a[4] == "X":
                f += 1
            l += 1
    if f == 2:
        return True
    else:
        return False
#Peadiagonaal
  
def x_peadiagonaalil(i):
    l = 0
    f = 0
    for a in i:
        if a[l] == "X":
            f += 1
        l += 1
    return int(f)
#Kõrvaldiagonaal

def x_korvaldiagonaalil(i):
    l = 4
    f = 0
    for a in i:
        if a[l] == "X":
            f += 1
        l -= 1
    return int(f)
#Diagonaalidemäng

def voitis_diagonaalidemangu(i):
    if x_peadiagonaalil(i) + x_korvaldiagonaalil(i) == 10:
        return True
    else:
        return False
#Täismäng

def voitis_taismangu(i):
    g = 0
    for a in i:
        f = 0
        f = a.count("X")
        g += f
    if g == 25:
        return True
    else:
        return False
