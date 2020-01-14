def tervitus(num):
    print("Võõrustaja: \"Tere!\"\nTäna {}. kord tervitada, mõtiskleb võõrustaja.\nKülaline: \"Tere, suur tänu kutse eest!\2".format(num))

inp = int(input("Sisestage külaliste arv: "))

for num in range(0,inp):
    tervitus(num+1)
