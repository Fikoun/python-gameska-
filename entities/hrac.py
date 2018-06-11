from entities.entity import *

class Hrac(Entity):
    def __init__(self, name, max_health, attack):
        super().__init__(name, max_health, attack)
        self.money = 0
        self.inventory = []

    """ Zbavit se těchto funkcí a předělta je do Entity
        def lowDamage(self):
            self.health += int(random.randint(int(self.health * 0.1), int(self.health * 0.15)))
            return int((self.attack * random.uniform(1, 1.3)))

        def midDamage(self):
            self.health += int(random.randint(int(self.health * 0.05), int(self.health * 0.08)))
            return int((self.attack * random.uniform(1.2, 1.4)))
    
        def highDamage(self):
            return int((self.attack * random.uniform(1.4, 1.8)))

        def showMoney(self):
            print(f"Tvoje Penize jsou {self.money}")
    """
    def showInv(self):
        for item in self.inventory:
            print (item.name)

    def add_item(self,item):
        self.inventory.append(item)
