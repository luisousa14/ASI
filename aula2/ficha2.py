# Exercicio 1
from statistics import mean

idades = [16, 18, 10, 28, 24, 26, 30, 46, 72, 65, 91]

#Menor idade
print(min(idades))
print("#"*60)

#Maior idade
print(max(idades))
print("#"*60)

#Media das idades
print(mean(idades))
print("#"*60)

#Media das idades entre 18 e 65 anos
total = 0
count = 0
for idade in idades:
    if 18 <= idade <= 65:
            total += idade
            count += 1

media = total / count
print(media)
print("#"*60)

######################################################################
#Exercicio 2

array = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]

#Mix das 2 proximas maneiras
notas = {}
for pos in array:
    notas[pos] = array.count(pos)

for chave,valor in notas.items():
    print("A nota %d apareceu %d vezes" % (chave, valor))

print("#"*60)
#Maneira mais simples, usar o array.count
for x in range(21):
    print("A nota %d apareceu %d vezes" % (x, array.count(x)))

print("#"*60)
#Maneira a usar os dicionarios
res = {}

for num in array:
    if num in res.keys():
        res[num] = int(res[num] + 1)
    else:
        res[num] = 1

print(res)
#print(res.items())
print("#"*60)

#################################################################
#Exercicio 3

data = input("Formato: DD/MM/AAAA \nData: ")

ano = data.split("/")[2]
idade = 2022 - int(ano)

if 0 <= idade <= 12:
    print("Criança %d" % (idade))
elif 13 <= idade <= 17:
    print("Juvem %d" % (idade))
elif 18 <= idade <= 64:
    print("Adulto %d" % (idade))
elif 65 <= idade:
    print("Sénior %d" % (idade))

print("#"*60)
##################################################################
#Exercicio 4

traducao = {'filme': ['film', 'movie'], 'locomotiva': ['locomotive', 'train'], 'pessoa': ['person', 'individual']}

print(traducao)

print("Possiveis traduções para locomotiva: " + ",".join(traducao['locomotiva']))







