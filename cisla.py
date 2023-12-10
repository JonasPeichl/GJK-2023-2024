
text = open("TestTrebuchet")
a = 0
b = 0
c= 0
d= 0
for i in range(4):
   prvni = False
   kod = text.readline()
   d = d + c
   for line in kod:
      while prvni == False:
         if line.isdigit():
            a += int(line)
            prvni = True
      if line.isdigit():
         b = 0
         b += int(line)
   c = a*10 + b
   print(c)

print(d)
         


      