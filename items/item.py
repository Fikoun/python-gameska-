class Item:

    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price




Items = []


def newItem(name, desc, price):
	novy_item = Item(name, desc, price)
	Items.append(novy_item)








