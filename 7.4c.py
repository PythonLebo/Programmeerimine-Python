for num in range(1,10):
    print(num)
    l=open("eluteenumber{}.txt".format(num),"w+")
    l.close()
def elutee(s):
    n = 0
    for i in s:
        if i != ".":
            n += int(i)
    if n < 10:
        return n
    else:
        return elutee(str(n))
fail = open("sunnikuupaevad.txt", encoding="UTF-8")
for rida in fail:
    f=open("eluteenumber{}.txt".format(elutee(rida.strip())), "a+")
    f.write("{}\n".format(rida.strip()))
    f.close()
fail.close()
