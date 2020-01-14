def nummerda(r1,r2):
    array = []
    for korrus in range(1,r1+1):
        temp = []
        for korter in range(1,r2+1):
            temp.append(str(korrus) + str(korter))
        array.append(temp)
    return array