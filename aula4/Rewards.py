import ReadLogFile


def RewardEmployee(visit):
    nomeUt1 = ""
    nomeUt2 = ""
    tempoMin = 10000000
    tempoMax = 0
    for key, value in visit.items():
        if key.__contains__("facebook"):
            for key1, value1 in value.items():
                if value1[1] < tempoMin:
                    tempoMin = value1[1]
                    nomeUt1 = key1
                if value1[1] > tempoMax:
                    tempoMax = value1[1]
                    nomeUt2 = key1

    dados = {"Minimo": (nomeUt1, tempoMin), "Maximo": (nomeUt2, tempoMax)}
    print("Employye of the month: %s with %d seconds in Facebook!!" % (nomeUt1, tempoMin))
    print("%s you do need to focus more on your work" % nomeUt2)
    return dados


print(RewardEmployee(ReadLogFile.Read("weblog.txt")))
