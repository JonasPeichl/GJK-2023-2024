import random
import getpass

x = random.randint(1, 100)  # Počítač vybere náhodné číslo od 1 do 100
pokusy = 0
max_pokusy = 10  # Maximální počet pokusů, můžete změnit podle potřeby

print("Hra Uhodni Číslo")
print("Hráč si zvolil náhodné číslo od 1 do 100.")
print(f"Máte maximálně {max_pokusy} pokusů.")

while True:
    hrac1_hadane_cislo = getpass.getpass("Hráč 1, napiš své číslo od 1 do 100 (zůstane skryté): ")
    
    try:
        hrac1_hadane_cislo = int(hrac1_hadane_cislo)
        if hrac1_hadane_cislo < 1 or hrac1_hadane_cislo > 100:
            print("Zadejte číslo v rozsahu od 1 do 100.")
            continue
    except ValueError:
        print("Zkus to znovu, zadejte platné číslo.")
        continue

    pokusy += 1

    if hrac1_hadane_cislo < x:
        print("Hádej větší číslo.")
    elif hrac1_hadane_cislo > x:
        print("Hádej menší číslo.")
    else:
        print(f"Správně! Hráč 1 uhodl číslo {x} ve {pokusy}. pokusu.")
        break

    if pokusy >= max_pokusy:
        print(f"Bohužel jste neprokázal dostatečnou dovednost k uhodnutí čísla. Hledané číslo bylo {x}.")
        break
