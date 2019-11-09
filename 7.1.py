replacements = {"Ä": "AE", "Õ": "OE", "Ö": "OE", "Ü": "UE"}
inp = str(input("Sisestage failinimi: "))
fail = open(inp, encoding="UTF-8")
for rida in fail:
    txt = str(rida).upper()
    print("".join([replacements.get(c, c) for c in txt]), end='')
fail.close()
