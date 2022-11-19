##############################################################################
#Exercicio 1

tif = """+351 123 321 123; +351 220 121 212;
+351 921 124 356;
+351 919 919 828;
+44 0 113 32 242"""

#Substituir todas as ocorrências de +351 para 00351

print(tif.replace("+351", "00351"))

##############################################################################
#Exercicio 2

frase = "8200123;Ana Maria;93221912;12/05/2000"

#criar a lista atraves de uma string separada por ;
lista = frase.split(";")

print(lista)

#imprimir o tamanho da lista
print(len(lista))

#Acrescentar "SOL" á lista
lista.append("SOL")

print(lista)
print(len(lista))

#Converter a lista final para string outra vez mas agora com ,
ultimaFrase = ",".join(lista)

print(ultimaFrase)

##############################################################################





