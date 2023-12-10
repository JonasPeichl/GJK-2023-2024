import re
cisla = "[1-9]"
text = open("TestTrebuchet")
kod = text.readlines()
for line in kod:
    print(line)
    print(re.findall(cisla,line))