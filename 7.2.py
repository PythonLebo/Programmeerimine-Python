from datetime import datetime
inp = str(input("Sisesta sissekande tekst: "))
fail = open("paevik.txt", "a+", encoding="UTF-8")
fail.write("{}\n{}\n\n".format(datetime.today(),inp))
fail.close()
