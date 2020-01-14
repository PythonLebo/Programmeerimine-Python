inp = str(input("Kas soovite istekohta ise valida (\"ise\") või loosida (\"loos\")? "))
if inp == "loos":
    import random
    rand = random.randint(1,3)
    if rand > 1: print("Istekoht loositi. Vahekäigukoht")
    else: print("Istekoht loositi. Aknakoht")
    

elif inp == "ise":
    ise = str(input("Kas soovite istuda akna ääres (\"aken\") või mitte (\"muu\")? "))
    if ise == "aken":
        print("Valisite ise. Aknakoht")
    elif ise == "muu":
        print("Valisite ise. Vahekäigukoht")
