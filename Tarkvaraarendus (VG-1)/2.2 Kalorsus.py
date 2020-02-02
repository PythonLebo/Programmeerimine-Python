fail = open("kalorid.txt", encoding="UTF-8")

toitude_tabel = []

for rida in fail: # iga rea jaoks failist
    korra_grammid = [] # kogume ühe toidukorra info
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        korra_grammid.append(int(osa)) # järjekordne info juurde

    toitude_tabel.append(korra_grammid) # toidukorra järjend juurde

fail.close()

kokku = 0

for array in toitude_tabel:
    kokku = kokku + array[0]*4 + array[1]*4 + array[2]*9

print(kokku)

########################################################

toitude_tabel = []
with open("kalorid.txt", encoding="UTF-8") as fail:
    for rida in fail:
        korra_grammid = []
        osad = rida.split()
        for osa in osad:
            korra_grammid.append(int(osa))
        toitude_tabel.append(korra_grammid)
cal = 0
for i in toitude_tabel:
    cal = cal + i[0]*4 + i[1]*4 + i[2]*9
print(cal)
