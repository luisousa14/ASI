import re

cc = "12345678 7 ZY8"

pattern = re.compile(r"^\d{8} \d [A-Z]{2}\d$")

if pattern.match(cc):
    print("CC Valido")
else:
    print("CC Invalido")

