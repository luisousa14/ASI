def ler(filename):
    with open(filename) as fp:
        vendas = {}
        for linha in fp:
            linha = linha.strip().split(";")
            hashtable = {}
            hashtable1 = {}
            if linha[0] in vendas.keys():
                hashtable = vendas[linha[0]]
                hashtable1["preco"] = linha[2]
                hashtable1["dataLancamento"] = linha[3]
                hashtable[linha[1]] = hashtable1
            else:
                hashtable1["preco"] = linha[2]
                hashtable1["dataLancamento"] = linha[3]
                hashtable[linha[1]] = hashtable1
                vendas[linha[0]] = hashtable
    fp.close()
    return vendas
