import re

with open("dados") as fp:
    masculino = {}
    feminino = {}
    patternM = re.compile(r";M;")
    pattern2 = re.compile(r"^")
    for linha in fp:
        if patternM.search(linha):
            linha = linha.strip().split(";")
            linha[3] = pattern2.sub("00351", linha[3])
            masculino[linha[3]] = linha[0]
        else:
            linha = linha.strip().split(";")
            linha[3] = pattern2.sub("00351", linha[3])
            feminino[linha[3]] = linha[0]
fp.close()

print(masculino)
print(feminino)

