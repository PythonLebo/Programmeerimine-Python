def eelarve(arv):
    return 55+10*arv
inp = str(input("Sisesta failinimi: "))
fail = open(inp,"r")
size,tuleb = 0,0
for rida in fail:
    size=size+1
    if not rida.find("+"):
        print(rida)
        tuleb = tuleb+1
fail.close()
print("Kutsutud on {} inimest".format(size))
print(tuleb,"inimest tuleb")
print("Maksimaalne eelarve: {} EUR".format(eelarve(size)))
print("Minimaalne eelarve: {} EUR".format(eelarve(tuleb)))
