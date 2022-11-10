import item
import numpy as np

class user_inventory(object):
    
    def __init__(self, console, user):
        self.user = user
        self.IOconsole = console
        self.min_size = 0
        self.current_size = 0
        self.max_size = 6
        self.armour = None
        self.helmet = None
        self.gloves = None
        self.weapon = None
        self.amulet = None
        self.rings = []
        self.item_inventory = {}
        self.default_inventory_items()
        
    # Add default player inventory
    def default_inventory_items(self):
        self.item_inventory_insert(item.Health_Potion(console=self.IOconsole, user=self.user))
        self.item_inventory_insert(item.Mana_Potion(console=self.IOconsole, user=self.user))
        
    # Get min inventory size
    def get_min_size(self):
        return self.min_size
    
    # Get current inventory size
    def get_current_size(self):
        return self.current_size
    
    # Get max inventory size
    def get_max_size(self):
        return self.max_size
    
    # Get player
    def get_armour(self):
        return self.armour
    
    # Set armour
    def set_armaour(self, armour):
        self.armour = armour
        
    # Get helmet
    def get_helmet(self):
        return self.helmet
    
    # Set helmet
    def set_helmet(self, helmet):
        self.helmet = helmet
        
    # Get gloves
    def get_gloves(self):
        return self.gloves
    
    # Set gloves
    def set_gloves(self, gloves):
        self.gloves = gloves
        
    # Get weapon
    def get_weapon(self):
        return weapon
    
    # Set weapon
    def set_weapon(self, weapon):
        self.weapon = weapon
        
    # Get amulet
    def get_amulet(self):
        return self.amulet
    
    # Set amulet
    def set_amulet(self, amulet):
        self.amulet = amulet

    # Get rings
    def get_rings(self):
        return self.rings
    
    # Set rings
    def set_rings(self, rings):
        self.rings = rings
        
    # Get items
    def get_items(self):
        return self.item_inventory
   
    # Get list of options
    def get_items_options(self):
        options = []
        for item in self.get_items().values():
            for target in item.get_target_options().values():
                options.append((item, target))
        return options
    
    # Get item
    def get_item(self, item_name):
        return self.item_inventory[item_name]
        
    def interface(self):
        self.display()
        return self.select_item_options()
        
    def display(self):
        print("---------------------------------------------------")
        print("{}'s Inventory:".format(self.user.get_name()))
        inventory_list = list(self.item_inventory.keys())
        menu_index = 1
        if len(inventory_list) == 0:
            print("Inventory is empty!")
            print("[1] Return to main player menu")
        else:
            for item in inventory_list:
                print("[{}] ".format(menu_index) + item + " ")
                menu_index += 1
            print("[{}] ".format(menu_index) + "Return to main player menu")
        print("---------------------------------------------------")
        
    def select_item_options(self):
        
        # Initialize choice variable to determine opposing player to target
        choice = 0
        item_list = list(self.get_items())
            
        # Let user select an item or exit menu
        while (choice < 1 or choice > len(item_list)+1):
            try:
                choice = int(input("Select an item or return back to main player option menu: "))
            except:
                print("Invalid Response")
                continue
            
        # Quit skills menu
        if choice == len(item_list)+1:
            return None
        
        else:
            item_name = item_list[choice-1]
        
            # Select item
            item = self.get_item(item_name)
        
            # Display item selected
            print("{} was selected!".format(item_name))
        
            return item
        
    # Use item from inventory 
    def item_inventory_select(self, item_name):
        self.item_inventory[item_name].use(self.user)
        del self.item_inventory[item_name]
        
    # Add item to inventory
    def item_inventory_insert(self, item):
        if self.get_current_size() < self.get_max_size():
            self.item_inventory[item.get_name()] = item
            self.current_size += 1
            if self.get_current_size() == self.get_max_size():
                print("Inventory has reach max limit!")
        else:
            print("Inventory Full!")
            
    # Git rid of inventory
    def item_inventory_drop(self, item):
        if self.item_inventory[item.get_name()]:
            del self.item_inventory[item.get_name()]
            self.current_size -= 1
        else:
            print("{} does not exist in {}'s inventory!".format(item.get_name(), self.user.get_name()))
            print("Current Inventory List:")
            print(list(self.item_inventory.keys()))
            