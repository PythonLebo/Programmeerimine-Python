from math import ceil

fail = open("raamatud.txt", encoding="UTF-8")

kirjandus_tabel = [] # Tühi järjend, kuhu lisame raamatud

for rida in fail:    # Iga rea jaoks failist
    raamat = []     # Kogume reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    osad = rida.split(":") # Jupitame rea semikooloni koha pealt

    pealkiri = osad[0].strip() # Eraldame pealkirja
    leheküljed = int(osad[1].strip()) # Eraldame lehekülgede arvu

    raamat.append(pealkiri) # Lisame reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    raamat.append(leheküljed)

    kirjandus_tabel.append(raamat) # Lisame raamatute järjendi kirjanduse tabelisse

fail.close()

aeg = 0

for raamat in kirjandus_tabel:
    kogu = 2*raamat[1]/60
    aeg = aeg+kogu

    if kogu > 8:
        päev = ceil(kogu/2)
        print("{} - {} päeva".format(raamat[0],päev))

print(round(aeg,1))