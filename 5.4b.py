fail1 = open("synnid.txt", encoding="UTF-8")
fail2 = open("surmad.txt", encoding="UTF-8")
synnid = []
surmad = []
iive = []
def tablefy(fail,t):
    for rida in fail:
        t.append(int(rida))
    fail.close()
tablefy(fail1,synnid)
tablefy(fail2,surmad)

for var in synnid:
    iive.append(var-surmad[synnid.index(var)])
print(iive)
for var in iive:
    if var > 0:
        print(iive.index(var)+1)
