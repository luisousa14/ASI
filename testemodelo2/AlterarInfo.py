import re

def adicionarDados(Alunos):

    pattern = re.compile(r"$")
    for chave, valor in Alunos.items():
        for chave1, valor1 in valor.items():
            valor[chave1] = pattern.sub(".0", valor1)

    print(Alunos)
