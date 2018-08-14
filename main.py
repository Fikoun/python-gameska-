from entities.hrac import *
from entities.enemy import *
from items.item import *
from funcs import *
from math import *

# Peníze jdou v boji do mínusu??? 
# Vytvořit metody v Hraci pro zvíšování statů.
# Předělat výpis itemů v obchodu na funkci: printTable()
# Projít komentáře v kódu a udělat potřebné úpravy.
# Napsat si vlastní komentáře k lepší orientaci v kódu.

# Vytvořit popisky a dokumentaci funkcí. (Janko)



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
            info_enemy = hrac.dealDamageTo(enemak)
            


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

            info_hrac= enemak.dealDamageTo(hrac)

        elif vyber == 2:
            info_enemy = hrac.dealDamageTo(enemak)
            

            if hrac.isDead():
                printBig("Skapal jsi")
                
                ztrata = ceil(random.uniform((hrac.money+1) *0.3,(hrac.money+1)*0.4))
                hrac.money -= ztrata
                
                print(f"-- Ztratil jsi -{ztrata}$ money ted mas {hrac.money}$ --")
                wait()
                break
            if enemak.isDead():
                printBig("Vyhral jsi")
                
                vyhra = ceil(random.uniform((hrac.money+10) * 0.25, (hrac.money+10) * 0.45))
                hrac.money += vyhra
                
                print(f"\t-- Vyhral jsi +{vyhra}$ money ted mas {hrac.money}$ --")
                wait()
                break

            info_hrac = enemak.dealDamageTo(hrac)
            

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

            vyhra = ceil(random.uniform((hrac.money+10) * 0.25, (hrac.money+10) * 0.45))
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
    print ("tve penize jsou: "+str({hrac.money}))
    koupeny_item = choice("Vyber item:",[item.name+getTabs(item.name, Items)+" -- "+str(item.price)+"$" for item in Items])-1
    clear()
    if (hrac.hasenoughmoney(Items[koupeny_item])== True):
        hrac.health += Items[koupeny_item].plus_hp
        hrac.attack += Items[koupeny_item].plus_dmg

        printBig("Uctenka E E T")

        hrac.add_item(Items[koupeny_item])
        print(f"--  Koupen item <{Items[koupeny_item].name}> za {Items[koupeny_item].price}$ tve hp se zvysili o <{Items[koupeny_item].plus_hp}> a dmg o <{Items[koupeny_item].plus_dmg}>")
    else:
        printBig("nemas dostatek penez")
        
    wait()
   

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


# LOAD ------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
print("---")
clear()
printBig("| ARENA - GAME |")
print("Made by: \t Drábek, Janko")
print("Version: \t 0.0.3v")
wait()
clear()

while True:
    printBig("Vloz jmeno ")
    print("< 3 az 9 znaku >")
    jmeno_zadane = input("\t> ")
    if (len(jmeno_zadane) <= 9) and (len(jmeno_zadane) >= 3):
        hrac = Hrac(jmeno_zadane,1000,200)
        break
    else:
        clear()
        print("Zadej jmeno dlouhe 3 az 9 znaku")
    


newItem("Dvořákova taška", "Krade", 50 , 20,20)
newItem("Ziggyho Hlava", "Boduje", 20, 10, 10)

newItem("Kopí", "Probodává", 50,0,30)
newItem("Meč", "Seká", 20,0,20)

newItem("Magická Hůl", "Čaruje", 50,10,40)
newItem("Kopřivova Rovnice", "počítá", 20,0,35)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


# MAIN LOOP ------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

while True:
    clear()
    vyber = choice("HLAVNI MENU :", ["Boj", "Obchod","Inventář", "Konec"])
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
