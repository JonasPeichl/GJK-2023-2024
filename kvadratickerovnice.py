import math
a=int(input("zadej a = "))
b=int(input("zadej b = "))
c=int(input("zadej c = "))

d=b**2-4*a*c

if d < 0:
    print("Žádné řešení")
    
elif d >= 0:
    D=math.sqrt(d)
    x=(-b+D)/2*a
    y=(-b-D)/2*a
    if x != y:
        print(f"x = {x} a y = {y}")
    elif x == y:
        print(f"y a x = {x}")