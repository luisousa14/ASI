def listagem(numAlunos, NomeAlunos):

    nomeAlunosAprova = []
    for numAluno, nomeAluno in NomeAlunos.items():
        for numAluno1, notas in numAlunos.items():
            for chave, valor in notas.items():
                if float(valor) >= 9.5 and numAluno == numAluno1 and chave == "ASI":
                    nomeAlunosAprova.append(nomeAluno)

    return nomeAlunosAprova



