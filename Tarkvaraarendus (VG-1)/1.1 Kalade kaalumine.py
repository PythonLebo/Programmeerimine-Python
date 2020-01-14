#Input
fileName = str(input())
alaM = int(input())
fti = float(input())
biggest = 0
#weight func
def kala_kaal(lenght,index):
    return round(lenght**3*index/100)
#File operations
file = open(fileName, encoding="UTF-8")
for row in file:
    if int(row) >= alaM:
        temp = kala_kaal(int(row),fti)
        if temp > biggest:
            biggest = temp
        print(temp)
    else:
        print("Kala lasti vette tagasi")
#Print the biggest fish
print(biggest*0.001)

file.close()