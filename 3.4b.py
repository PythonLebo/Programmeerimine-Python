from random import randint
inp = int(input("sisestage visketabavuse protsent: "))
hit = 0
for num in range(0,1000):
    if randint(1,100) <= inp:
        hit = hit+1
        print("vise tabas")
    else: print("vise mööda")
print("Tabas {} viset".format(hit))
