import random
x = random.randint(0, 100)
while True:
    pokus = input("Napiš číslo od 1 od 100   ")
    try:
        pokus = int(pokus)
    except ValueError:
        print ("Zkus to znovu")
        continue
    if pokus < x:
        print("Větší")
    elif pokus > x:
        print("Menší")
    else:
        print(f"Správně, číslo bylo {x} ")
        break
