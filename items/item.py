class Item:

    def __init__(self, name, desc, price, plus_hp, plus_dmg):
        self.name = name
        self.desc = desc
        self.price = price
        self.plus_dmg = plus_dmg
        self.plus_hp = plus_hp



Items = []


def newItem(name, desc, price):
	novy_item = Item(name, desc, price)
	Items.append(novy_item)




