# a)

nifs = {}

with open("dados.txt") as fp:
    for linha in fp:
        linha = linha.strip().split(";")
        hashtable = {}
        hashtable[linha[1]] = linha[2]
        if nifs.keys().__contains__(linha[0]):
            nifs[linha[0]].update(hashtable)
        else:
            nifs[linha[0]] = hashtable
fp.close()

print(nifs)
print("#"*60)

# b)
nif = input("Insira o seu NIF: ")
for key, value in nifs[nif].items():
    print("Matricula: %s    IUC: %s" % (key, value))

