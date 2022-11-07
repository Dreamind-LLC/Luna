import numpy as np

class Item(object):
    def __init__(self, user, name):
        self.user = user
        self.name = name


    def get_name(self):
        return self.name


    def get_target_options(self):
        pass


    def display(self):
        print("---------------------------------------------------")
        print(" Target Options:")
        target_list = list(self.get_target_options())
        menu_index = 1
        for target in target_list:
            print(" [{}] ".format(menu_index) + target + " ")
            menu_index += 1
        print(" [{}] ".format(menu_index) + "Return to main player menu")
        print("---------------------------------------------------")


    def interface(self):
        
        # Display skills
        self.display()
    
        # Initialize choice variable to determine what skill to use
        choice = 0
        
        # List all the targers
        target_list = list(self.get_target_options().values())
        
        # Let user select a target
        while (choice < 1 or choice > (len(target_list)+1)):
            try:
                choice = int(input("Select a target or return back to main player option menu: "))
            except:
                print("Invalid Response")
                continue
        
        # Quit skill menu
        if choice == len(target_list)+1:
            return None
        
        else:
            # Select skill
            target = target_list[choice-1]
        
            return target


    def __del__(self):
        del self


class Potion(Item):
    def __init__(self, user, name, quantity):
        Item.__init__(self, user, name)
        self.quantity = quantity


    def get_name(self):
        return self.name


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity += quantity
        if self.quantity <= 0:
            self.user.inventory.item_inventory_drop(self)

     
    def get_target_options(self):
        pass


class Health_Potion(Potion):
    def __init__(self, user, name="Health Potion", health_cost=20, quantity=1):
        Potion.__init__(self, user, name, quantity)
        self.healing_cost = health_cost


    def get_target_options(self):
        return self.user.team.get_teammembers()


    def execute(self, target):
        if self.quantity > 0:
            target.set_health(self.healing_cost)
            print(" {} was healed with {:.2f} health points using a {}!".format(target.get_name(), self.healing_cost, self.get_name()))
            self.set_quantity(-1)
            

class Mana_Potion(Potion):
    def __init__(self, user, name="Mana Potion", mana_cost=20, quantity=1):
        Potion.__init__(self, user, name, quantity)
        self.mana_cost = mana_cost


    def get_target_options(self):
        return self.user.team.get_teammembers()


    def execute(self, target):
        if self.quantity > 0:
            target.set_mana(self.mana_cost)
            print(" {} was restored with {:.2f} mana points using a {}!".format(target.get_name(), self.mana_cost, self.get_name()))
            self.set_quantity(-1)


class crest(Item):
    pass


class armour(Item):
    pass


class gauntlet(Item):
    pass


class greaves(Item):
    pass


class amulet(Item):
    pass


class ring(Item):
    pass