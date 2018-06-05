class Entity:
    def __init__(self,name,health,attack):
        self.name= name
        self.health = health
        self.attack = attack

    def staty(self):
        print(self.name)
        print(self.health)
        print(self.attack)

    def jeMrtvy(self):
        if (self.health <= 0):
            return True
        else:
            return False

    def ubratZivoty(self, kolik):
        self.health -= kolik
        return f"{self.osloveni}  {kolik} ted jsou zivoty na {self.health}"

    # def randomDamage(self,zaklad, nasobek):
    #     return zaklad.randint(0.😎,(1.2)*nasobek
    #
    #
    # def randomHeal(self, zaklad, nasobek):
    #
    #     return zaklad.randint(0.1),(0.12)*nasobek
