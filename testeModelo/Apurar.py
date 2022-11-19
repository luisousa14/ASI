def acumulado(condutores):
    acumulados = {}
    for chave, valor in condutores.items():
        for chave1, valor1 in valor.items():
            for chave2, valor2 in valor1.items():
                if chave in acumulados.keys():
                    acumulados[chave] += float(valor2[1].split("â")[0])
                else:
                    acumulados[chave] = float(valor2[1].split("â")[0])

    return acumulados