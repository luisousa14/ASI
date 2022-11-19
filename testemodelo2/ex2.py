import re

string = "Luis Corte-Real Sousa"

pattern = re.compile(r"([A-Z])[a-z]+[\s\W]?")

nome = "Luis Corte-Real Sousa"
asda = pattern.finditer(nome)
final = ""

while True:
    try:
        item = next(asda).group(1).lower()
        final += str(item) + "."
    except StopIteration:
        break

print(final)