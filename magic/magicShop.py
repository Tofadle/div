#magicShop.py - a fantasy magic shop where you can buy, upgrade and equip gear
import random, weaponNamer

def main():
    """Runs the store"""
    #Initialize store with empty inventory and 400 cash
    store = inventory([], 400)
    player = inventory([], 50)

    #Initialize weapons and add to store inventory
    sword1 = Weapon("Giant Broadsword", 14, 20)
    sword2 = Weapon("Shortsword", 7, 10)
    axe1 = Weapon("Skullsplitter", 19, 25)
    knives1 = Weapon("Throwing knives", 7, 5)
    trinket = Trinket("Magic Trinket", 0, 50)
    initialWeapons = [sword1, sword2, axe1, knives1, trinket]
    for weapon in initialWeapons:
        store.addToInventory(weapon)
    

    end = False
    welcomeMessage()
    while not end:
        reply = input("> ")
        if reply == "browse":
            browse(store, player)
        elif reply == "exit":
            end = True
        elif reply == "inventory":
            print(player.checkInventory())
        elif reply == "balance":
            print(player.checkBalance())
        elif reply == "help":
            welcomeMessage()
        else:
            print("Please input a valid option")
            continue
        
def browse(store, player):#Make browse not automatically display next item when inspecting item
    choice = print("Inspect, buy, or stop browsing?\n(\'next\' to move to next item)\n")
    for item in store.inventory:
        print(f"{item}")
        choice = input("> ")
        if choice.lower() == "inspect":
            print(f"{item.name}: a {item.kind}, doing {item.dmg} damage.\n")
        elif choice.lower() == "buy": #When you buy the loop skips several items?
            player.buy(item, store)
        elif choice.lower() == "stop":
            return
        elif choice.lower() == "next":
            continue
        else:
            return
    print("That's all our wares")
    
def welcomeMessage():
    print("Welcome to our fine store\n")
    print("\'browse\' to look at our wares\n")
    print("\'inventory' to browse player inventory\n")
    print("\'balance\' to check you money\n")
    print("\'exit\' to leave\n")
    print("\'help\' to display this text again.")

class Weapon:
    def __init__(self, name, dmg, price):
        self.name = name
        self.dmg = dmg
        self.price = price

    def __str__(self):
        return f"{self.name}"

#NOTE: I suspect weaponNamer won't make a unique weapon every time. fix this later
class Trinket:
    def createWeapon():
        #Generate name on the wordlists
        name = weaponNamer.weaponNamer
        #generate dmg based on nameList
        dmg = weaponNamer.damageGenerator(name)
        #generate price based on adjective
        price = weaponNamer.priceGenerator(name)
        return Weapon(name, dmg, price)

    def __str__(self):
        return "A magical trinket, which has the ability to create weapons"


class inventory:
    #inventory class for both store and player
    def __init__(self, inventory, balance):
        self.inventory = inventory
        self._balance = balance

    def addToInventory(self, item):
        self.inventory.append(item)
    
    def removeFromInventory(self, item):
        self.inventory.remove(item)

    def browseInventory(self):
        for item in self.inventory:
            print(item)

    def buy(self, item, seller):
        print(f"{item} costs {item.price}. Proceed? y/n\n")
        proceed = input("> ")
        if proceed.lower() == "y" and self._balance >= item.price:
            self.addToInventory(item)
            seller.removeFromInventory(item)
            self.removeBalance(item.price)
            seller.addBalance(item.price)
        elif self._balance < item.price:
            print("Sorry! Not enough funds")
        elif proceed.lower() == "n":
            pass

    def sell(self, inventory):
        pass    

    def addBalance(self, amount):
        self._balance += amount

    def removeBalance(self, amount):
        self._balance -= amount

    def checkBalance(self):
        return f"{self._balance}"

    def checkInventory(self):
        for item in self.inventory:
            if item == None:
                self.inventory.remove(item)
            print(item)



if __name__ == "__main__":
    main()
