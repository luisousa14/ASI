#a)
hastable = {}

with open('input.txt') as fp:
    for linha in fp:
        linha = linha.strip().split(";")
        hastable[linha[0]] = linha[1]
fp.close()

print(hastable)
print("*"*60)

##################################################
#b)

numero = input("Insira o número de aluno:")
print("Nome:", hastable[numero])




