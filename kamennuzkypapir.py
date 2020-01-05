from random import randrange

odpoved = "ano"
while odpoved == "ano":
    print ("Hraj \"kámen\"/ \"nůžky\"/ papír\":")
    hrac = input("Hráč: ")
    pocitac = randrange(3)
    if pocitac == 0:
        print ("Počítač: kámen")
    elif pocitac == 1:
        print ("Počítač: nůžky")
    else:
        print ("Počítač: papír")

    if (hrac == "kámen" and pocitac == 0) or (hrac == "nůžky" and pocitac == 1) or (hrac == "papír" and pocitac == 2):
        print ("Plichta")
    elif (hrac == "kámen" and pocitac == 1) or (hrac == "nůžky" and pocitac == 2) or (hrac == "papír" and pocitac == 0):
        print ("Vyhrál jsi!")
    elif (hrac == "kámen" and pocitac == 2) or (hrac == "nůžky" and pocitac == 0) or (hrac == "papír" and pocitac == 1):
        print ("Počítač vyhrál!")
    else:
        print ("Zadal jsi něco špatně.")
    odpoved = input("Chceš to zkusit znovu? ")