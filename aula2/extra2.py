#A
metros = float(input("Inserir um numero metros: "))
print("Resultado em centimetros: ", metros * 100)
print("#"*60)

#B
numero = int(input("Numero para formar a tabuada: "))
for n in range(1,11):
    print("%d x %d = %d" % (numero, n, numero*n))
print("#"*60)

#C
nota1 = int(input("Nota1: "))
nota2 = int(input("Nota2: "))
print("Média: ", (nota1+nota2)/2)
print("#"*60)

#D
for num in range(5,101):
    if num % 7 == 0 and num % 5 != 0:
        print(num)
print("#"*60)

#E
x = int(input("Valor: "))
if x > 0:
    print("Positivo")
elif x < 0:
    print("Negativo")
else:
    print("Neutro")
print("#"*60)
