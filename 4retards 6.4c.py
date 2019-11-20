kuud = ["jaanuar", "veebruar", "märts", "april", "mai", "juuni", "juuli", "august", "september", "oktoober","november", "detsember"] #kuud tabelis
def kuu_nimi(num):
    return kuud[num-1] #v6tab kuude tabelist 6ige kuu. Pythoni tabelid hakkavad 0-ist mitte yhest nii, et on vaja lahutada 1 et saada 6ige asi
  
def kuupäev_sõnena(kuu):
    splited = kuu.split(".") #splitib stringi
    s6na = kuu_nimi(int(splited[1])) #v6tab teise spilted stringi
    return  "{}. {} {}. a".format(splited[0],s6na,splited[2]) #foramtib vastuse 6igesti

print(kuupäev_sõnena(str(input("Sisesta kuupäev kujuö DD.MM.YYYY: ")))) #kysib kasutajalt inputi j
