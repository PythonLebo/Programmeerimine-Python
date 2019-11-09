kuud = ["jaanuar", "veebruar", "märts", "april", "mai", "juuni", "juuli", "august", "september", "oktoober","november", "detsember"]
import re
def kuu_nimi(num):
    return kuud[num-1]
    
def kuupäev_sõnena(kuu):
    s6na = kuu_nimi(int(kuu.split(".")[1]))
    return  "{}. a".format(re.sub('\.\d*\.', ". {} ".format(s6na), kuu))

print(kuupäev_sõnena(str(input("Sisesta kuupäev kujuö DD.MM.YYYY: "))))    
