import re
from datetime import datetime

now = datetime.now()
hoje = "0" + str(now.day) + "/" + str(now.month) + "/" + str(now.year)
print(hoje)

patternData = re.compile(r"(0[1-9]|1\d|2\d|3[0-1])\/(0[1-9]|1[0-2])\/\d{4}")
patternMonatante = re.compile(r"(-\d+|\d+)(\.\d{2})$")

with open("transacoes") as fp:
    credito = 0
    debito = 0
    for linha in fp:
        linha = linha.strip().split(";")
        if patternData.match(linha[0]) and patternMonatante.match(linha[2]) and patternData.match(hoje) and linha[0] == hoje:
            if float(linha[2]) > 0:
                credito += float(linha[2])
            else:
                debito += float(linha[2])
            print(linha)

    print("Credito: ", credito)
    print("Debito: ", debito)
