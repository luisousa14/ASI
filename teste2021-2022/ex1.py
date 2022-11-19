import re

test_str = ("{\n"
"authID: bGVpMTIzCg==\n"
"ContaOrigem: PT50 0010 1234 12345678901 01\n"
"ContaDestino: PT50 0018 4334 62245778183 19\n"
"Montante: 5000.12€\n"
"}")

pattern = re.compile(r"^{\nauthID: [a-zA-Z]*==\nContaOrigem: PT50 \d{4} \d{4} \d{11} \d{2}\nContaDestino: PT50 \d{4} \d{4} \d{11} \d{2}\nMontante: [0-9]{1,10}(\.[0-9]{0,2})€\n}$")
pattern1 = re.compile(r"Montante: 5[0-9]{3}")


if pattern.match(test_str):
    if pattern1.search(test_str):
        print("valido alterta 5000€")
    print("valido")
