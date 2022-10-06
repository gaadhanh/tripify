import re

val="Pythzon Is An object oriented Language123456 Pytzon"
valstr=re.findall("Is|an",val)
print(valstr)