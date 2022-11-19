from statistics import mean


def media(Alunos):
    notasUC = {}
    for numAluno, notas in Alunos.items():
        for siglaUc, valores in notas.items():
            if siglaUc in notasUC.keys():
                notasUC[siglaUc].append(int(notas[siglaUc]))
            else:
                notasUC[siglaUc] = [int(notas[siglaUc])]

    for chave, valor in notasUC.items():
        notasUC[chave] = mean(valor)

    return notasUC