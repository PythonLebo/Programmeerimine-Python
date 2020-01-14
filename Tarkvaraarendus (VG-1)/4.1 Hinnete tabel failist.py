def keskmised(mArray):
    for aine in mArray:
        temp = 0
        for hinne in aine[1:]:
            temp = temp + int(hinne)
        print(f"{aine[0]}: {round(temp/(len(aine)-1),1)}")

file = open("hinded.csv", encoding="UTF-8")
matrix = []
for rida in file:
    row = []
    array = rida.split(",")

    for i in array:
        row.append(i)

    matrix.append(row)

file.close()

keskmised(matrix)