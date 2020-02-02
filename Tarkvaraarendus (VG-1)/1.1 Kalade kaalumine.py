#Input
fileName = str(input())
alaM = int(input())
fti = float(input())
biggest = 0
#weight func
def kala_kaal(lenght,index):
    return round(lenght**3*index/100)
#File operations
file = open(fileName, encoding="UTF-8")
for row in file:
    if int(row) >= alaM:
        temp = kala_kaal(int(row),fti)
        if temp > biggest:
            biggest = temp
        print(temp)
    else:
        print("Kala lasti vette tagasi")
#Print the biggest fish
print(biggest*0.001)

file.close()

###################################################

def kala_kaal(i,o):
    p = i**3 * o / 100
    return int(round(p, 0))
fnimi = input("Sisestage failinimi: ")
alam = int(input("Sisestage püügi alamõõt: "))
fti = float(input("Sisestage fultoni tüsedusindeks: "))
pikkus = []
kras = 0
with open(fnimi) as fail:
    for rida in fail:
        pikkus.append(int(rida))
for e in pikkus:
    if e >= alam:
        print("Püütud kala kaaluga {} grammi".format(kala_kaal(e, fti)))
        if kala_kaal(e, fti)> kras:
            kras = kala_kaal(e, fti)
    else:
        print("Kala lasti vette tagasi")
print("Kõige raskem püütud kala: {} kg".format(float(kras)/1000))
