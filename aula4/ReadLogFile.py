import funcoes

def Read(string):
    visit = {}
    with open(string) as fp:
        for linha in fp:
            linha = linha.strip().split(";")
            if linha[0] in visit.keys():
                hashtable = visit[linha[0]]
                if linha[1] in hashtable.keys():
                    hashtable[linha[1]][0] += 1
                    hashtable[linha[1]][1] += funcoes.toTime(linha[3])
                else:
                    dados = [1, funcoes.toTime(linha[3])]
                    hashtable[linha[1]] = dados
            else:
                hashtable = {}
                dados = [1, funcoes.toTime(linha[3])]
                hashtable[linha[1]] = dados
                visit[linha[0]] = hashtable
    fp.close()
    return visit


print(Read("weblog.txt"))
