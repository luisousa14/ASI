#a)
hastable = {}
alunos = {}

with open('alunos.txt') as fp:
    for linha in fp:
        linha = linha.strip().split(";")
        if linha[3] == "F":
            hastable[linha[0]] = linha[1:]
        alunos[linha[0]] = linha[1:]

fp.close()

print(hastable)
print("#"*60)

##########################################################
# b)

num = input("Insira o numero de aluno: ")
print("Numero: %s\nNome: %s\nIdade: %s\nGenero: %s\nTelemovel: %s" % (num, alunos[num][0], alunos[num][1], alunos[num][2], alunos[num][3]))
print("#"*60)

##########################################################
#c)
def mediaIdade(dicionario):
    count = 0
    soma = 0
    for value in dicionario.values():
        soma += float(value[1])
        count += 1
    return float(soma / count)

print("A media de idades dos alunos é: ", mediaIdade(alunos))






