import re

pattern = re.compile(r"[a-z]")
print(len(pattern.findall("Ola mundo")))