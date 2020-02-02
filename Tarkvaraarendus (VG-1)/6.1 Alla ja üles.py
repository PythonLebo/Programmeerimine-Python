def alla_ules(i):
    if i <= 0:
        print("Põhi!")
    else:
        print(i)
        alla_ules(i-2)
        print(i-1)
