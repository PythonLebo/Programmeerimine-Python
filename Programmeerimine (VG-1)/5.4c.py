from datetime import *
inp = str(input("Sisestage failinimi: "))
fail = open(inp, encoding="UTF-8")
t = []
for rida in fail:
    t.append(str(rida))
fail.close()
print(t[datetime.now().day-1])
