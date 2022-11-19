import re

string = "Luis Borges Sousa"
pattern = re.compile(r"^[A-Z][a-z]+(\s[A-Z][a-z]+)*$")

if pattern.match(string):
    print("Valido")
else:
    print("Invalido")










