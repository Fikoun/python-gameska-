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
        if len(str(i.name)) > longest:
            longest = len(str(i.name))
    res = ""
    for _ in range(1+round((longest-len(str(txt)))/5.65)):
        res += "\t"
    return res
    # Zbavit se této finkce a nahradit ji.


def printTable(content, border=False, spacing=3):
    bor = '|' if border else ''
    separ = "+"
    longest = [0] * len(content[0])
    for i in range(0, len(content[0])):
        for radek in content:
            if longest[i] < len(str(radek[i])):
                longest[i] = len(str(radek[i]))
        separ += ('-'*(longest[i]+spacing+2))+'+'

    for x, radek in enumerate(content):
        print()
        print((separ.replace("-","=") if x==0 or x==1 else separ) if border else '')  
        for i, bunka in enumerate(radek):
            print(bor+str(bunka),' '*((longest[i]-len(str(bunka)))+spacing),bor if i==len(radek)-1 else '', end="")
    print()
    print((separ.replace("-","=") if x==0 else separ) if border else '')  
        

def objectToList(insts, attrs):
    attrs = attrs.split(" ")
    return [ [getattr(inst, attr) for attr in attrs] for inst in insts ] 

# PŘÍKLAD
# printTable([

#     ["gjkhgkjPrvek1", "ztweuizweriuzretiufwztferuzpisek", "ghjfCena"],
#     ["hhPrvek2", "ghjhhPopisek2", "Cenaa"],
#     ["Prvek3", "Popisek3", "ggCenaaa"],
#     ["gjkgjhPrvek4", "hPopisek", "ggghjgfjhgfghjfCenaaa"],
#     ["ghjPrvek5", "gjkhhPopisek5", "fCenaaaa"],
# ],True, 0)
