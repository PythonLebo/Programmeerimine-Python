vanus = int(input("Sisestage enda vanus:" ))
sugu = str(input("Sisestage enda sugu:" )).lower()
treening = int(input("Sisestage treeningu tüüp:" ))

def calc(prec,num):
  return round(prec*num/100)

def func(x):
  if treening == 1:
    print("Pulsisagedus peaks olema vahemikus {} kuni {}".format(calc(50,x),calc(70,x)))
  elif treening == 2:
    print("Pulsisagedus peaks olema vahemikus {} kuni {}".format(calc(70,x),calc(80,x)))
  elif treening == 3:
    print("Pulsisagedus peaks olema vahemikus {} kuni {}".format(calc(80,x),calc(87,x)))

if sugu == "n":
    func(206-(88*vanus/100))
elif sugu == "m":
    func(220-vanus)
