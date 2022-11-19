def topPrecipitacao(temp):
    topPreci = {}
    for chave, valor in temp.items():
        for chave1, valor1 in valor.items():
            if chave in topPreci.keys():
                topPreci[chave] += int(valor1["precipitacao"])
            else:
                topPreci[chave] = int(valor1["precipitacao"])

    max = 0
    dist = ""
    for key, value in topPreci.items():
        if value > max:
            max = value
            dist = key

    return dist, max

def minTemp(temp):
    minTemp = {}
    min1 = 1000000
    for chave, valor in temp.items():
        for chave1, valor1 in valor.items():
            if int(valor1["temperatura"]) < min1:
                minTemp[chave1] = int(valor1["temperatura"])


    min = 1000000
    dist = ""
    for key, value in minTemp.items():
        if value < min:
            min = value
            dist = key

    return dist, min