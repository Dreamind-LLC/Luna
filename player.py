import inventory as inv
import skillstree as sktr
import numpy as np

# Create basic player object
class Player(object):
    
    # Initialize player object
    def __init__(self, name, team, health=100.0, mana=100.0, speed=100.0, accuracy=15.0):
        self.name = name
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.speed = int(np.random.normal(speed, 0.03*speed))
        self.accuracy = np.random.normal(accuracy, 0.03*accuracy)
        self.roll_number = 0
        self.team = team
        self.inventory = inv.user_inventory(self)
        self.skillstree = sktr.skillstree(self)
    
    # Get player's name
    def get_name(self):
        return self.name
    
    # Get player's health
    def get_health(self):
        return self.health

    # Set player's health
    def set_health(self, health):
        self.health += health
        
        # If health less than zero set to zero
        if self.get_health() <= 0:
            
            # Display player that was killed
            print("{} was eliminated!!".format(self.get_name()))
            
            # Delete player from player list
            self.team.remove_teammember(self)
            
        # If health more than max health set to max health
        if self.get_health() > self.get_max_health():
            self.health = self.get_max_health()
            
    def get_max_health(self):
        return self.max_health
    
    def set_max_health(self, max_health):
        self.max_health = max_health
            
    # Get player's mana
    def get_mana(self):
        return self.mana
    
    # Set player's mana
    def set_mana(self, mana):
        self.mana += mana
        
        # If mana is below zero set to zero
        if self.get_mana() <= 0:
            self.mana = 0
            
        # If mana is above max mana set to max mana
        if self.get_mana() > self.get_max_mana():
            self.mana = self.get_max_mana()
            
    def get_max_mana(self):
        return self.max_mana
    
    def set_max_mana(self, max_mana):
        self.max_mana = max_mana
    
    # Get player's speed
    def get_speed(self):
        return self.speed
    
    # Set player's speed
    def set_speed(self, speed):
        self.speed += speed
    
    # Get player's accuracy
    def get_accuracy(self):
        return self.accuracy
    
    # Set player's accuracy
    def set_accuracy(self, accuracy):
        self.accuracy += accuracy

    # Get all player attributes
    def get_all_attr(self):
        attr_list = []
        attr_list.append(self.get_name())
        attr_list.append(self.get_health())
        attr_list.append(self.get_mana())
        attr_list.append(self.get_speed())
        attr_list.append(self.get_accuracy())
        return attr_list
    
    # Get player's roll number
    def get_roll_number(self):
        return self.roll_number
    
    # Set player's roll number
    def set_roll_number(self, num):
        self.roll_number = num
    
    # Determine how likely the player hits opposing enemy
    def attack_rating(self):
        
        # Use an inverse absolute normal distribution (between 0 and 1)
        mu = 0
        sigma = 1.0 - (self.get_accuracy()/100.00)
        
        # Round number to a single decimal
        x = np.round_(np.random.normal(mu, sigma), decimals=1)
        
        # If larger than 0 inverse it
        if x > 0:
            x = -x
        
        # Shift distribution number by 1
        x = 1 + x
        
        # if less than zero set x to zero
        if x < 0:
            x = 0
            
        # Return attack rating
        return x
    
    # Determine actions player should use
    def select_actions(self):
       
        # If basic enemy - perform basic attack
        options = self.list_options()
        choice = np.random.choice(len(options),1)
        action, target = options[choice[0]]
        return action, target
   
    def list_options(self):
        return self.skillstree.get_skills_options() + self.inventory.get_items_options()
   
    def rank_actions(self):
        pass
       
    # Determine player action
    def action(self):
       
        # Keep track of player action
        action = None
       
        # List player options
        action, target = self.select_actions()
       
        if action and target:
            action.execute(target)
            input("Press the Enter Key to continue.")

    """
    def ai_options(self):
        # E - number of enemies
        # M - mana
        # D - defense rating
        # A - accuracy/attack rating?
        # S - speed
        # H - health
        # P - attack power
        u = (E*E*M*(E*D*E*A*E*S+E*H*P))/(H*H*M*(H*D*E*A*H*S+H*H*P))
    """

# Create a hero object
class Hero(Player):
    
    # Initialize hero object
    def __init__(self, name, team):
        Player.__init__(self, name, team)

    # List options human player can make
    def action(self):
   
        # Give player options
        action = None
        option = None
        valid_input = False
        
        # Keep prompting user for a valid option 
        while (valid_input==False):
            try:
                print("[1]: Action")
                print("[2]: Inventory")
                print("[3]: Exit")
                option = int(input("Input: "))
            except:
                print("Invalid Response")
                continue
            
            # User chooses an action
            if option == 1: 
                action = self.skillstree.interface()
            
            # User chooses to look up inventory
            elif option == 2:
                action = self.inventory.interface()

            elif option == 3:
                exit()
                
            if action:
                
                # User chooses target
                target = action.interface()
                
                if target:
                    valid_input = True
            
        # Need to select target option
        action.execute(target)
        input("Press the Enter Key to continue.")
    
    def display_menu(self):
        pass
    
    def confirm_action(self):
        pass
    
    