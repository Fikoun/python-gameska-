class Entity:
    def __init__(self, name, max_health, attack):
        self.max_health = max_health
        self.health = max_health
        self.name = name
        self.attack = attack

    def printStats(self):
        # Vymyslet tuto funkci
        pass

    
    def getDamage(self, kolik):
        self.health -= kolik
        # Nahradit všechny ty low mid a highDamge metody v Hracovi
        # pomocí techto funkcí getDamage a dealDamage.
        # Zajistit aby životy nešli do nuly.
       
    def getHealing(self, kolik):
        self.health += kolik
        # Zajistit aby životy ví jak max.

    def dealDamageTo(self, opponent):
        # Nahradit všechny ty low mid a highDamge metody v Hracovi
        # pomocí techto funkcí getDamage a dealDamage.
        opponent.getDamage(self.attack)
        return f"{self.name} ubral {self.attack}"

    def restoreHealth(self):
        self.health = self.max_health


    def isDead(self):
        if (self.health <= 0):
            return True
        else:
            return False

  

   
        