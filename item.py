import numpy as np

class Item(object):
    """
    The Item class creates objects that players can interact with
    to increase their stats or use to affect gameplay. Each
    item has an interface to select among several possible 
    target players and an execution method to implement action.
    """

    def __init__(self, console, user, name):
        self.IOconsole = console
        self.user = user
        self.name = name


    def get_name(self):
        return self.name


    def get_target_options(self):
        pass


    # Player's item interface to select from available targets
    def interface(self):
        
        # Display skills
        title = " Target Options:"
        self.IOconsole.display_title(title)

        # List all the targets
        target_list = list(self.get_target_options().values())
        target_str_list = list(self.get_target_options())
        target_str_list.append("Return to main player menu")
    
        # Initialize choice variable to determine what skill to use
        choice = 0
        
        # Let user select a target
        while (choice < 1 or choice > (len(target_list)+1)):
            try:
                title = "Select a target or return back to main player option menu: "
                choice = int(self.IOconsole.display_menu(title, target_str_list))
            except:
                self.IOconsole.display_text("Invalid Response")
                continue
        
        # Quit skill menu
        if choice == len(target_list)+1:
            return None
        
        # Select skill
        else:
            target = target_list[choice-1]
        
            return target


    def __del__(self):
        del self


class Potion(Item):
    def __init__(self, console, user, name, quantity):
        Item.__init__(self, console, user, name)
        self.IOconsole = console
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
    def __init__(self, console, user, name="Health Potion", health_cost=20, quantity=1):
        Potion.__init__(self, console, user, name, quantity)
        self.healing_cost = health_cost


    def get_target_options(self):
        return self.user.team.get_teammembers()


    def execute(self, target):

        if self.quantity > 0:
            target.set_health(self.healing_cost)
            text = " {} was healed with {:.2f} health points using a {}!".format(target.get_name(), self.healing_cost, self.get_name())
            self.IOconsole.display_text(text)
            self.set_quantity(-1)
        else:
            text = " {} was already at full health!".format(target.get_name())
            self.IOconsole.display_text(text)


class Mana_Potion(Potion):
    def __init__(self, console, user, name="Mana Potion", mana_cost=20, quantity=1):
        Potion.__init__(self, console, user, name, quantity)
        self.mana_cost = mana_cost


    def get_target_options(self):
        return self.user.team.get_teammembers()


    def execute(self, target):

        if self.quantity > 0:
            target.set_mana(self.mana_cost)
            text = " {} was restored with {:.2f} mana points using a {}!".format(target.get_name(), self.mana_cost, self.get_name())
            self.IOconsole.display_text(text)
            self.set_quantity(-1)
        else:
            text = " {} was already at full mana!".format(target.get_name())
            self.IOconsole.display_text(text)


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