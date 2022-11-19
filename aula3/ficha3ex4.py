# a)

nifsVeiculos = {}
nifsImoveis = {}

with open("dados2.txt") as fp:
    for linha in fp:
        linha = linha.strip().split(";")
        hashtable = {}
        hashtable2 = {}
        hashtable[linha[2]] = linha[3]
        if linha[5] and linha[6] != "":
            hashtable2[linha[4]] = linha[5:]
        if nifsImoveis.keys().__contains__(linha[0]):
            nifsImoveis[linha[0]].update(hashtable2)
        else:
            nifsImoveis[linha[0]] = hashtable2
        if nifsVeiculos.keys().__contains__(linha[0]):
            nifsVeiculos[linha[0]].update(hashtable)
        else:
            nifsVeiculos[linha[0]] = hashtable
fp.close()

print(nifsVeiculos)
print(nifsImoveis)
print("#" * 60)


#####################################################
# b)
def maxTaxaImi(nifsImoveis):
    maxNif = ""
    maxTaxa = float(0)
    for key, value in nifsImoveis.items():
        for key2, value2 in value.items():
            if maxTaxa < float(value2[1]):
                maxTaxa = float(value2[1])
                maxNif = key
    print("O NIF que paga mais taxa é %s com o valor de: %f" % (maxNif, maxTaxa))

maxTaxaImi(nifsImoveis)

print("#"*60)
#######################################################
#c)

def maxImpostos(nifsImoveis, nifsVeiculos):
    nifsImpostos = {}
    for key, value in nifsImoveis.items():
        for key2, value2 in value.items():
            if nifsImpostos.keys().__contains__(key):
                nifsImpostos[key] += float(float(value2[0]) * float(value2[1]))
            else:
                nifsImpostos[key] = float(float(value2[0]) * float(value2[1]))

    for key, value in nifsVeiculos.items():
        for key2, value2 in value.items():
            if nifsImpostos.keys().__contains__(key):
                nifsImpostos[key] += float(value2)
            else:
                nifsImpostos[key] = float(value2)

    for key, value in nifsImpostos.items():
        print("NIF: %s com os impostos de %d" % (key, value))

maxImpostos(nifsImoveis, nifsVeiculos)


