import getpass
x = int(getpass.getpass("Napiš tvé číslo od 1 od 100   "))
while True:
    pokus = input("Napiš číslo od 1 od 100   ")
    try:
        pokus = int(pokus)
        if pokus < x:
            print("Větší")
        elif pokus > x:
            print("Menší")
        else:
            print(f"Správně, číslo bylo {x} ")
            break
    except ValueError:
        print ("Zkus to znovu")
        continue