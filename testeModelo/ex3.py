import re

patternNome = re.compile(r"^[A-Z][a-z]+(\s[A-Z][a-z]+)*$")
patternData = re.compile(r"\d{4}\-(0[1-9]|1[0-2])\-(0[1-9]|1\d|2\d|3[0-1])")
patternNumero = re.compile(r"00351 9(1|2|3|6)\d{7}")

String = "Jose Maria Almeida;00351 962341234;1997-12-19"

strings = String.strip().split(";")

if patternNumero.match(strings[1]) and patternData.match(strings[2]) and patternNome.match(strings[0]):
    print("Valido")