inp = int(input())
fail = open("mootorrattad.txt", encoding="UTF-8")
mootorrattad = []
for rida in fail:
    mootorrattad.append(int(rida))
fail.close()
print(mootorrattad[inp-1])
