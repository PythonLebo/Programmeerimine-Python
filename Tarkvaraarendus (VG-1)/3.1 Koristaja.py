fail = open("toad.txt", encoding="UTF-8")

tubade_tabel = []

for rida in fail: # iga rea jaoks failist
    korruse_toad = [] # kogume ühe korruse tubasid
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        korruse_toad.append(int(osa)) # järjekordne tuba juurde

    tubade_tabel.append(korruse_toad) # korruse tubade järjend juurde

fail.close()

for korrus, toad in enumerate(tubade_tabel):
    if (korrus % 2) != 0:
        for tuba in toad:
            if (tuba % 2) == 0:
                print(tuba)
                
###############################################################################

tubade_tabel = []
with open("toad.txt", encoding="UTF-8") as fail:
    for rida in fail:
        korruse_toad = []
        osad = rida.split()
        for osa in osad:
            if int(osa) % 2 == 0:
                korruse_toad.append(int(osa))
        tubade_tabel.append(korruse_toad)
for i in tubade_tabel:
    if tubade_tabel.index(i) % 2 != 0:
        for a in i:
            print(a)
