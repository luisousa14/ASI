import re

pattern = re.compile(r"(([0-9]+)|(\(-[0-9]+\)))(\+|-|\*|\/)(([0-9]+)|(\(-[0-9]+\)))((\+|-|\*|\/)(([0-9]+)|(\(-[0-9]+\))))*")

string = "5+172+5-5/2*5"
string1 = "5+-172+5-5/2*5"
string2 = "1+(-10)+1*10/2"


if pattern.match(string1):
    print("OK: ", eval(string1))