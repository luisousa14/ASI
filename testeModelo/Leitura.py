def ler(file):
    with open(file) as fp:
        condutores = {}
        for linha in fp:
            linha = linha.strip().split(";")
            veiculos = {}
            if linha[0] in condutores.keys():
                veiculos = condutores[linha[0]]
                if linha[1] in veiculos.keys():
                    contraOrd = veiculos[linha[1]]
                    contraOrd[linha[2]] = linha[3:6]
                    veiculos[linha[1]] = contraOrd
                else:
                    contraOrd = {}
                    contraOrd[linha[2]] = linha[3:6]
                    veiculos[linha[1]] = contraOrd
            else:
                contraOrd = {}
                contraOrd[linha[2]] = linha[3:6]
                veiculos[linha[1]] = contraOrd
                condutores[linha[0]] = veiculos

    fp.close()
    return condutores
