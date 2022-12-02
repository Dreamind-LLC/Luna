import item
import numpy as np

class inventory(object):
    """
    The inventory class is a data strucutre that keeps track of all
    the items that an individual players currently has.
    """
    
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

        # Keep track of available actions of items and players
        options = []

        # For each item in inventory
        for item in self.get_items().values():

            # For player in available targets
            for target in item.get_target_options().values():

                # Update availabl actions list
                options.append((item, target))

        return options
    
    # Get item
    def get_item(self, item_name):
        return self.item_inventory[item_name]
        
    # Player's inventory interface to select from available items
    def interface(self):

        # Display menu
        title = "{}'s Inventory:".format(self.user.get_name())
        inventory_list = list(self.item_inventory.keys())
        inventory_list.append("Return to main player menu")
        choice = self.IOconsole.display_menu(title, inventory_list)
        if len(inventory_list) == 0:
            self.IOconsole.display_text("Inventory is empty!")

        # Quit skills menu
        if choice == len(inventory_list):
            return None
        
        # Select item
        else:
            item_name = inventory_list[choice-1]
            item = self.get_item(item_name)
        
            # Display item selected
            text = " {} was selected!".format(item_name)
            self.IOconsole.display_text(text)
        
            return item  
        
    # Use item from inventory 
    def item_inventory_select(self, item_name):
        self.item_inventory[item_name].use(self.user)
        del self.item_inventory[item_name]
    

    # Add item to inventory
    def item_inventory_insert(self, item):

        # Determine if inventory is full
        if self.get_current_size() < self.get_max_size():
            self.item_inventory[item.get_name()] = item
            self.current_size += 1
            if self.get_current_size() == self.get_max_size():
                self.IOconsole.display_text(" Inventory has reach max limit!")
        # Else
        else:
            self.IOconsole.display_text(" Inventory Full!")
    
    # Git rid of inventory
    def item_inventory_drop(self, item):

        # If item exist in inventory
        if self.item_inventory[item.get_name()]:
            del self.item_inventory[item.get_name()]
            self.current_size -= 1

        # Else item does not exist
        else:
            text1 = " {} does not exist in {}'s inventory!".format(item.get_name(), self.user.get_name())
            text2 = " Current Inventory List:"
            text3 = list(self.item_inventory.keys())
            self.IOconsole.display_text(text1)
            self.IOconsole.display_text(text2)
            self.IOconsole.display_text(text3)
            