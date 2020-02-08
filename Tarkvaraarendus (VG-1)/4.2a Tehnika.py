with open("tehnika.txt") as file:
    for rida in file.read().splitlines():
        array = rida.split()
        dif = int(array[7]) - int(array[1])
        if dif > 10:
            print(f'{array[0]} - {dif}%')
###################################################
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
