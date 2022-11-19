
def vendasMes(vendas):
    vendasMes = {}
    for chave, valor in vendas.items():
        for chav1, valor1 in valor.items():
            if chave in vendasMes.keys():
                vendasMes[chave] += float(valor1["preco"])
            else:
                vendasMes[chave] = float(valor1["preco"])

    return vendasMes

def vendasLivro(vendas):
    vendasLivro = {}
    for chave, valor in vendas.items():
        for chave1, valor1 in valor.items():
            if chave1 in vendasLivro.keys():
                vendasLivro[chave1] += 1
            else:
                vendasLivro[chave1] = 1

    return vendasLivro

def livroAlancar(vendas):
    livroAlancar = []
    for chave, valor in vendas.items():
        for chave1, valor1 in valor.items():
            if valor1["dataLancamento"] == "":
                livroAlancar.append(chave1)

    return livroAlancar