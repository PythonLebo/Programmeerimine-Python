fail = open("tulemused.txt", encoding="UTF-8")

tulemuste_tabel = []
#Võiks kasutada key, value süsteemi
for rida in fail: # iga rea jaoks failist
    seti_punktid = [] # kogume ühe seti punkte
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        seti_punktid.append(int(osa)) # järjekordsed punktid juurde

    tulemuste_tabel.append(seti_punktid) # seti punktide järjend juurde
fail.close()

eesti = 0
soome = 0

for setP in tulemuste_tabel:
    if setP[0] > setP[1]:
        eesti = eesti+1
    else:
        soome = soome+1

if eesti > soome:
    print("Eesti võitis {}-{}".format(eesti,soome))
else:
    print("Soome võitis {}-{}".format(soome,eesti))