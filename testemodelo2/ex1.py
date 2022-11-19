import re

string = "823213@estg.ipp.pt,123213@estg.ipp.pt,323213@estg.ipp.pt"

pattern = re.compile(r",")

strings = pattern.split(string)

for email in strings:
    print(email)
