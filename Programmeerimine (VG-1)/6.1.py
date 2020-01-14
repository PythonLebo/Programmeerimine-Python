inp1 = int(input("Mitu korda soovite reklaamlauset kuvada? "))
inp2 = str(input("Sisestage reklaamlause: "))
def banner(txt):
    return txt.upper()

for num in range(0,inp1):
    print(banner(inp2))
