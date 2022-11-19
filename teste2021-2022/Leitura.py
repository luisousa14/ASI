def ler(dados):
    temp = {}
    with open(dados) as fp:
        for linha in fp:
            linha = linha.strip().split(";")
            hashtable = {}
            hashtable1 = {}
            if linha[0] in temp.keys():
                hashtable = temp[linha[0]]
                hashtable1["temperatura"] = linha[3]
                hashtable1["precipitacao"] = linha[2]
                hashtable[linha[1]] = hashtable1
            else:
                hashtable1["temperatura"] = linha[3]
                hashtable1["precipitacao"] = linha[2]
                hashtable[linha[1]] = hashtable1
                temp[linha[0]] = hashtable
    fp.close()
    return temp

