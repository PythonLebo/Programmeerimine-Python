from urllib.request import urlopen
inp1 = str(input("Sisestage kuu: ")).lower()
inp2 = int(input("Sisestage päev: "))
kuu = inp1.replace("ä","a")
print(urlopen("http://kodu.ut.ee/~eno/mooc/"+kuu).read().decode().splitlines()[inp2-1])
