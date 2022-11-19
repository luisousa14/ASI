precoBase = int(input("Insira o preço base: "))

precoFinal = float((precoBase * 0.23) - 10)
string = "precoFinal = (precoBase * 23%) - 10"
string = string.replace("precoBase", str(precoBase))

print(string + "\nResiltado: %f" % (precoFinal))

