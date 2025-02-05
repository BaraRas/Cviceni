"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Barbora Rašticová
email: rasticova.barbora@seznam.cz
"""

import random

def vytvor_nahodne_cislo():
    """Vytvoří čtyřciferné unikátní náhodné čílo, které nesmí začínat nulou"""
    nahodne_cislo = random.sample(range(0, 10), 4)

    if nahodne_cislo[0] == 0: 
        nove_cislo = random.randint(1, 9)
        while nove_cislo in nahodne_cislo:
            nove_cislo = random.randint(1, 9)
        nahodne_cislo[0] = nove_cislo
    
    return "".join(map(str,nahodne_cislo))

def over_vstup(vstup):
    """Ověří, zda vstup uživatele splňuje požadavky (4 cifry, unikátní, nezačíná nulou, jen čísla)"""
    if len(vstup) != 4: 
        return "Entered number is not 4 digits..."
    elif len(vstup) != len(set(vstup)): 
        return "Entered number contains duplicates..."
    elif not vstup.isdigit(): 
        return "You entered a non numeric characters.."
    elif int(vstup[0]) == 0: 
        return "Entered number starts with zero..."
    return None
    
def vypocitej_bulls_cows(vstup, cislo):
    """Spočítá bulls (správná čísla na správném místě) a cows (správná čísla na špatném místě)."""
    bull = 0
    cow = 0

    for i in range(4):
        if vstup[i] == cislo[i]:
            bull += 1
        if vstup[i] in cislo:
            cow +=1
    return bull, (cow - bull)

def bulls_and_cows():
    print('''Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you, 
Let's play a bulls and cows game.
-----------------------------------------------''')
    cislo = vytvor_nahodne_cislo()
    pocet_odhadu = 0 #počítání počtu odhadů uživatele
    vstup = ""

    print("Enter a number:")

    while vstup != cislo:
        pocet_odhadu +=1
        print("-----------------------------------------------")
        vstup = input(">>> ")

        chyba = over_vstup(vstup)
        if chyba:
            print(chyba)
            continue

        bull, cow = vypocitej_bulls_cows(vstup, cislo)
        print(bull, "bull" if bull == 1 else "bulls", ",", cow, "cow" if cow == 1 else "cows")

    return pocet_odhadu
pocet = bulls_and_cows()

print(" ")  
print("Correct, you've guessed the right number")
print("in", pocet, "guesses!")
print("-----------------------------------------------")
print("That's amazing!")

   






    








