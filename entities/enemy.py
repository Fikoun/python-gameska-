from entities.entity import *
import random
class Enemy(Entity):
    def __init__(self, name, max_health, attack):
        super().__init__(name, max_health, attack)

    """ Zbavit se této funkcí a předělta je do Entity   
	    def damage(self):
	        return int(self.attack * random.uniform(1.2, 1.5) )
	"""

enemy_names = [
"Pepik","Arnold","Ondrej",
"Cucek","Lolec","Janko",
"Recman","Ciggy","Ziggy",
"Bednář","Dvořák","Kraby"
]

def newEnemy(baseHP, baseAT):
	return Enemy(random.choice(enemy_names), 
		random.randint(int(baseHP * (4/7)),int(baseHP * (9/8))),
        random.randint(int(baseAT * (4/7)),int(baseAT * (9/8)) ))
	# Vyladit tuhle funkci.

