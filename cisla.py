
text = open("TestTrebuchet")

prvni = False
for i in range(4):
   kod = text.readline()
   for line in kod:
      while prvni == False:
         if line.isdigit():
            print(line)
            prvni = True


      