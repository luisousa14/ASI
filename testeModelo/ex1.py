import re

string = "192.168.1.0/32"
pattern = re.compile(r"(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-5]{2})\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-5]{2})\/([0-9]|1[0-9]|2[0-9]|3[0-2])$")

if pattern.match(string):
    print("valido")

