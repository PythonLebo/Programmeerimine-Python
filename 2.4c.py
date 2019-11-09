import math
inim = int(input("Inimeste arv: "))
koht = int(input("Kohtade arv: "))
print("Busse vaja:",math.ceil(inim/koht))
if inim%koht == 0:
    print("Viimases bussis inimsesi: ",koht)
else: print("Viimases bussis inimsesi:",inim%koht)
