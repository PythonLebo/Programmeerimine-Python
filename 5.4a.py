inp = str(input("Palun sisestage failinimi: "))
fail = open(inp, encoding="UTF-8")
t = []
for rida in fail:
    t.append(str(rida))
fail.close()
print("Muusikapalade valik:")
for var in t:
    print("{}. {}".format(t.index(var)+1,var))
inp2 = int(input("Valige laulu järjekorranumber: "))
print(t[inp2-1])
