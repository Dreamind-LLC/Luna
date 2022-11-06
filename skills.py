import numpy as np

class Action(object):
    def __init__(self, user, action_name):
        self.action_name = action_name
        self.user = user
        
    def get_name(self):
        return self.action_name

    def get_user(self):
        return self.user
    
    def get_target_options(self):
        return self.user.team.get_enemy_teammembers()
        
    def execute(self, target):
        pass
    
    def display(self):
        print(96*"-")
        print("Target Options:")
        target_list = list(self.get_target_options())
        menu_index = 1
        for target in target_list:
            print("[{}]: ".format(menu_index) + target + " ")
            menu_index += 1
        print("[{}]: ".format(menu_index) + "Return to main player menu")
        print(96*"-")
    
    def interface(self):
        
        # Display skills
        self.display()
    
        # Initialize choice variable to determine what skill to use
        choice = 0
        
        # List all the targets
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

class Attack(Action):
    def __init__(self, user, action_name, damage):
        Action.__init__(self, user, action_name)
        self.attack_damage = damage
    
class Bash(Attack):
    def __init__(self, user):
        Attack.__init__(self, user, action_name='Bash', damage=10.0)
        
    def get_target_options(self):
        return self.user.team.get_enemy_teammembers()
        
    def execute(self, target): 
        
        # Actual damage inflicted based on how accurate player is
        total_damage = np.round_(self.attack_damage * self.user.attack_rating(), decimals=2)
        
        # Display damage to console
        if total_damage > 0:
            print("{} was dealt {:.2f} of {} damage!".format(target.get_name(), total_damage, self.get_name()))
        else:
            print("{} missed {}!!".format(self.get_name(), target.get_name()))
            
        # Assign damage to opposing player
        target.set_health(-total_damage)
    
class Spell(Action):
    def __init__(self, user, action_name, magic_type, mana_cost):
        Action.__init__(self, user, action_name)
        self.magic_type = magic_type
        self.spell_cost = mana_cost   

        
class FireBlast(Spell):
    def __init__(self, user):
        Spell.__init__(self, user, action_name='Fire Blast', magic_type='Fire', mana_cost=20)
        
    def get_target_options(self):
        return self.user.team.get_enemy_teammembers()
        
    def execute(self, target):
        
        # Mana cost
        if self.user.get_mana() < self.spell_cost:
            mana_cost = self.user.get_mana()
        else:
            mana_cost = self.spell_cost
            
        # Determine spell damage
        # spell_damage = np.round_(mana_cost * self.user.attack_rating(), decimals=2)
        total_damage = np.random.normal(mana_cost, 0.1*mana_cost)  
        
        # Display damage results to console
        if total_damage > 0:
            # Update to print multiple targets
            print("{} was dealt {:.2f} of {} damage!".format(target.get_name(), total_damage, self.get_name()))
        else:
            print("{} missed {}!!".format(self.get_name(), target.get_name()))
            
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(-total_damage)

class IceBlast(Spell):
    def __init__(self, user):
        Spell.__init__(self, user, action_name='Ice Blast', magic_type='Ice', mana_cost=5)
        
    def get_target_options(self):
        return self.user.team.get_enemy_teammembers()
        
    def execute(self, target):
        
        # Mana cost
        if self.user.get_mana() < self.spell_cost:
            mana_cost = self.user.get_mana()
        else:
            mana_cost = self.spell_cost
            
        # Determine spell damage
        # spell_damage = np.round_(mana_cost * self.user.attack_rating(), decimals=2)
        total_damage = np.random.normal(mana_cost, 0.1*mana_cost) 
        
        # Display damage results to console
        if total_damage > 0:
            # Update to print multiple targets
            print("{} was dealt {:.2f} of {} damage!".format(target.get_name(), total_damage, self.get_name()))
        else:
            print("{} missed {}!!".format(self.get_name(), target.get_name()))
            
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(-total_damage)
        
class LightingBolt(Spell):
    def __init__(self, user):
        Spell.__init__(self, user, action_name='Lighting Bolt', magic_type='Lighting', mana_cost=10)
        
    def get_target_options(self):
        return self.user.team.get_enemy_teammembers()
        
    def execute(self, target):
        
        # Mana cost
        if self.user.get_mana() < self.spell_cost:
            mana_cost = self.user.get_mana()
        else:
            mana_cost = self.spell_cost
            
        # Determine spell damage
        # spell_damage = np.round_(mana_cost * self.user.attack_rating(), decimals=2)
        total_damage = np.random.normal(mana_cost, 0.1*mana_cost) 
        
        # Display damage results to console
        if total_damage > 0:
            # Update to print multiple targets
            print("{} was dealt {:.2f} of {} damage!".format(target.get_name(), total_damage, self.get_name()))
        else:
            print("{} missed {}!!".format(self.get_name(), target.get_name()))
            
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(-total_damage) 
        
class Venom(Spell):
    def __init__(self, user):
        Spell.__init__(self, user, action_name='Venom', magic_type='Poison', mana_cost=10)
        
    def get_target_options(self):
        return self.user.team.get_enemy_teammembers()
        
    def execute(self, target):
        
        # Mana cost
        if self.user.get_mana() < self.spell_cost:
            mana_cost = self.user.get_mana()
        else:
            mana_cost = self.spell_cost
            
        # Determine spell damage
        total_damage = np.random.normal(mana_cost, 0.1*mana_cost) 
        
        # Display damage results to console
        if total_damage > 0:
            # Update to print multiple targets
            print("{} was dealt {:.2f} of {} damage!".format(target.get_name(), total_damage, self.get_name()))
        else:
            print("{} missed {}!!".format(self.get_name(), target.get_name()))
            
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(-total_damage) 
        
class Healing(Spell):
    def __init__(self, user):
        Spell.__init__(self, user, action_name='Healing', magic_type='Basic', mana_cost=20)
        
    def get_target_options(self):
        return self.user.team.get_teammembers()
        
    def execute(self, target):
        if self.user.get_mana() < self.spell_cost:
            mana_cost = self.user.get_mana()
        else:
            mana_cost = self.spell_cost
        
        hp = np.random.normal(mana_cost, 0.1*mana_cost)
        
        print("{} was healed with {:.2f} health points!".format(target.get_name(), hp))
        
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(hp)
        
class ManaShield(Spell):
    def __init__(self, user):
        Spell.__init__(self, user, action_name='Mana Shield', magic_type='Basic', mana_cost=20)
        
    def get_target_options(self):
        return self.user.team.get_teammembers()
        
    def execute(self, target):
        if self.user.get_mana() < self.spell_cost:
            mana_cost = self.user.get_mana()
        else:
            mana_cost = self.spell_cost
            
        defense = np.random.normal(mana_cost, 0.1*mana_cost)  
        
        print("{} has raised {:.2f} mana shield!".format(target.get_name(), defense))
        
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_defense(defense) 
        