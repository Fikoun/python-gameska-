from entities.entity import *
from entities.hrac import *
from entities.enemy import *
from items.item import *
from funcs import *
from math import *
# BOJ ------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
def boj():
    enemak = newEnemy(hrac.health, hrac.attack)
    info_enemy = ""
    info_hrac =  ""
    while True:

        print(f"{enemak.name} má\t{enemak.health}/{enemak.max_health} HP\t-- {info_enemy}")
        print(f"Ty máš\t\t{hrac.health}/{hrac.max_health} HP\t-- {info_hrac}")
    
        vyber = choice("Vyber AKCI :", ["Lehky utok", "Silny utok", "Vyléčit"])
        clear()

        if vyber == 1:
            info_hrac= enemak.dealDamageTo(hrac)
            info_enemy = hrac.dealDamageTo(enemak)

        elif vyber == 2:
            info_hrac= enemak.dealDamageTo(hrac)
            info_enemy = hrac.dealDamageTo(enemak)

        elif vyber == 3:
            info_enemy = ""
            info_hrac = "HEAL"

        if hrac.isDead():
            printBig("Skapal jsi")
            
            ztrata = ceil(random.uniform((hrac.money+1) *0.3,(hrac.money+1)*0.4))
            hrac.money -= ztrata
            
            print(f"-- Ztratil jsi -{ztrata}$ money ted mas {hrac.money}$ --")
            wait()
            break
        if enemak.isDead():
            printBig("Vyhral jsi")
            
            vyhra = ceil(random.uniform((hrac.money+1) * 0.25, (hrac.money+1) * 0.45))
            hrac.money += vyhra
            
            print(f"\t-- Vyhral jsi +{vyhra}$ money ted mas {hrac.money}$ --")
            wait()
            break
    hrac.restoreHealth()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


# OBCHOD ------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


def obchod():
    while True:
        clear()
        vyber = choice("OBCHOD :", ["Koupit Item", "Odejít z Obchodu"])
        clear()
        if vyber == 1:
            while True:
               vyber_itemu = choice("Vyber item:",[item.name+getTabs(item.name, Items)+" -- "+str(item.price)+"$" for item in Items]) 
               clear()
               printBig("Koupit")
               
               print(f"--  Koupen item <{Items[vyber_itemu-1].name}> za {Items[vyber_itemu-1].price}$  --")
               wait()
               clear()
               break
        elif vyber == 2:
            return
    # Peníze se neodečítají ani nekontrolují.
    # Itemů a jejic přidávání hráčovi se musí dodělat.
    # Dalé jejich effekt na hru jako třeba zvíší attack.
   

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


# LOAD ------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
print("---")
clear()
printBig("| ARENA - GAME |")
print("Made by: \t Drábek, Janko")
print("Version: \t 0.0.1v")
wait()
clear()

printBig("Vloz jmeno")
hrac = Hrac(input("\t> "),1000 ,200)
clear()


newItem("Dvořákova taška", "Krade", 50)
newItem("Ziggyho Hlava", "Boduje", 20)

newItem("Kopí", "Probodává", 50)
newItem("Meč", "Seká", 20)

newItem("Magická Hůl", "Čaruje", 50)
newItem("Kopřivova Rovnice", "počítá", 20)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


# MAIN LOOP ------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

while True:
    clear()
    vyber = choice("HLAVNI MENU :", ["Boj", "Obchod","Inventář", "Konec", ])
    clear()
    if vyber == 1:
        boj()
    elif vyber == 2:
        obchod()
    elif vyber == 3:
        hrac.showInv()
        wait()
    elif vyber == 4:
        exit(1)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------