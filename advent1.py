import re
cisla = "[1-9]"
text = open("TrebuchetLauncher")
kod = text.readlines()
for line in kod:
    print(line)
    print(re.findall(cisla,line))