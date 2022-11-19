import re

pattern = re.compile(r"\d{4}\/(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[0-1])\s(0\d|1\d|2[0-4])\:(0\d|[0-5]\d)\:([0-5]\d)")
string = "2016/01/12 23:32:23"

if pattern.match(string):
    print("valido")
