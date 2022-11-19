def ler(filename):
    with open(filename) as fp:
        Alunos = {}
        NomeAlunos = {}
        for linha in fp:
            linha = linha.strip().split(";")
            notas = {}
            NomeAlunos[linha[1]] = linha[2]
            if linha[1] in Alunos.keys():
                notas = Alunos[linha[1]]
                notas[linha[0]] = linha[3]
            else:
                notas[linha[0]] = linha[3]
                Alunos[linha[1]] = notas
    fp.close()

    return Alunos, NomeAlunos

