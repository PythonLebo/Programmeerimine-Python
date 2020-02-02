tehnika = []
with open("tehnika.txt", encoding="UTF-8") as fail:
    for rida in fail:
        osad = rida.strip()
        e = []
        for osa in osad.split():
            e.append(osa)
        tehnika.append(e)
for i in tehnika:
    diff = int(i[7]) - int(i[1])
    if diff > 10:
        print("{} - {}%".format(i[0], diff))
