import pyfiglet
import os
from math import *

# Clears console window
clear = lambda : os.system('cls')

def clear():
    os.system('cls')

# Prints multiple options and handles input.
def choice(title, opts):
    error = False;
    while True:

        printBig(title)
        if error:
            print(error)

        for i,opt in enumerate(opts):
            print("\t>",i+1,"< -- ",opt)

        try:
            volba = int(input("\t> "))
        except Exception as ex:
            clear()
            error =  '!! -> Použij číslo <- !!'
            continue

        if volba > 0 and volba <= len(opts):
            return volba
        else:
            clear()
            error =  '!! -> Toto není platná možnost <- !!'

# Stop program and waits for user input.
def wait():
    input("\nPress [ENTER] to continue")

# Uses pyfiglet module to print ASCCI TEXT.
def printBig(txt):
    print(pyfiglet.figlet_format(txt, font="small"))

# Uses pyfiglet module to print ASCCI TEXT.
def getTabs(txt,all):
    longest = 0;
    for i in all:
        if len(i.name) > longest:
            longest = len(i.name)
    res = ""
    for _ in range(1+round((longest-len(txt))/5.65)):
        res += "\t"
    return res
    # Zbavit se této finkce a nahradit ji.


def table(border, spacing, content):
    bor = '|' if border else ''
    separ = "+"
    longest = [0] * len(content[0])
    for i in range(0, len(content[0])):
        for radek in content:
            if longest[i] < len(radek[i]):
                longest[i] = len(radek[i])
        separ += ('-'*(longest[i]+spacing+2))+'+'

    for radek in content:
        print()
        print(separ if border else '')  
        for i, bunka in enumerate(radek):
            print(bor+bunka,' '*((longest[i]-len(bunka))+spacing),bor if i==len(radek)-1 else '', end="")
    print()
    print(separ if border else '')  


# PŘÍKLAD
# table(True, 0,[

#     ["gjkhgkjPrvek1", "ztweuizweriuzretiufwztferuzpisek", "ghjfCena"],
#     ["hhPrvek2", "ghjhhPopisek2", "Cenaa"],
#     ["Prvek3", "Popisek3", "ggCenaaa"],
#     ["gjkgjhPrvek4", "hPopisek", "ggghjgfjhgfghjfCenaaa"],
#     ["ghjPrvek5", "gjkhhPopisek5", "fCenaaaa"],
# ])

