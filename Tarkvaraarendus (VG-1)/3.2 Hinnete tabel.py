def keskmised(mArray):
    newArray = []
    for aine in mArray:
        temp = 0
        for hinne in aine[1:]:
            temp = temp + hinne
        newArray.append([aine[0],round(temp/(len(aine)-1),1)])
    return newArray