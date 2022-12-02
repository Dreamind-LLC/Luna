import numpy as np

class Action(object):
    """
    The Action class is used to perform individual player actions
    and spells. Each action has an interface to select among
    several possible target players and an execution method
    to implement action.
    """

    def __init__(self, console, user, action_name):
        self.IOconsole = console
        self.action_name = action_name
        self.user = user
        
    # Get action name
    def get_name(self):
        return self.action_name

    # Get user
    def get_user(self):
        return self.user
    
    # Get target options
    def get_target_options(self):
        return self.user.team.get_enemy_teammembers()
        
    # Default execute method
    def execute(self, target):
        print("Execution Error")
        exit()
    
    # Player's skills interface to select from available targets
    def interface(self):
        
        # Display skills
        title = " Target Options:"
        target_list = list(self.get_target_options().values())
        target_str_list = list(self.get_target_options())
        target_str_list.append("Return to main player menu")
    
        # Initialize choice variable to determine what skill to use
        choice = 0
        
        # Let user select a target
        while (choice < 1 or choice > (len(target_list)+1)):
            try:
                title = " Select a target or return back to main player option menu: "
                choice = int(self.IOconsole.display_menu(title, target_str_list))
            except:
                self.IOconsole.display_text(" Invalid Response")
                continue

        
        # Quit skill menu
        if choice == len(target_list)+1:
            return None
        
        # Select skill
        else:
            target = target_list[choice-1]
            return target


class Attack(Action):
    def __init__(self, console, user, action_name, damage):
        Action.__init__(self, console, user, action_name)
        self.attack_damage = damage

    # Display damage done to target
    def display_damage(self, user, target, damage):

        if damage > 0:
            text = " {}'s {} dealt {} {:.2f} of damage!".format(user.get_name(), self.get_name(), target.get_name(), damage)
        else:
            text = " {}'s {} missed {}!!".format(user.get_name(), self.get_name(), target.get_name())

        self.IOconsole.display_text(text)
    
    
class Bash(Attack):
    def __init__(self, console, user):
        Attack.__init__(self, console, user, action_name='Bash', damage=10.0)
        
    def get_target_options(self):
        return self.user.team.get_enemy_teammembers()
        
    def execute(self, target): 
        
        # Actual damage inflicted based on how accurate player is
        total_damage = np.round_(self.attack_damage * self.user.attack_rating(), decimals=2)
        
        # Display damage to console
        self.display_damage(self.user, target, total_damage)

        # Assign damage to opposing player
        target.set_health(-total_damage)
    

# TO DO - Update spells based on player resistance attributes and spell effects
class Spell(Action):
    def __init__(self, console, user, action_name, magic_type, mana_cost):
        Action.__init__(self, console, user, action_name)
        self.magic_type = magic_type
        self.spell_cost = mana_cost   


class Attack_Spell(Spell):

    def display_damage(self, user, target, damage):

        if damage > 0:
            text = " {}'s {} dealt {} {:.2f} of damage!".format(user.get_name(), self.get_name(), target.get_name(), damage)
        else:
            text = " {}'s {} missed {}!!".format(user.get_name(), self.get_name(), target.get_name())

        self.IOconsole.display_text(text)
        

class FireBlast(Attack_Spell):
    def __init__(self, console, user):
        Spell.__init__(self, console, user, action_name='Fire Blast', magic_type='Fire', mana_cost=20)
        
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
        self.display_damage(self.user, target, total_damage)
            
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(-total_damage)


class IceBlast(Attack_Spell):
    def __init__(self, console, user):
        Spell.__init__(self, console, user, action_name='Ice Blast', magic_type='Ice', mana_cost=5)
        
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
        self.display_damage(self.user, target, total_damage)
            
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(-total_damage)
        

class LightingBolt(Attack_Spell):
    def __init__(self, console, user):
        Spell.__init__(self, console, user, action_name='Lighting Bolt', magic_type='Lighting', mana_cost=10)
        
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
        self.display_damage(self.user, target, total_damage)
            
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(-total_damage) 
     

class Venom(Attack_Spell):
    def __init__(self, console, user):
        Spell.__init__(self, console, user, action_name='Venom', magic_type='Poison', mana_cost=10)
        
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
        self.display_damage(self.user, target, total_damage)
            
        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(-total_damage) 
       

class Healing(Spell):
    def __init__(self, console, user):
        Spell.__init__(self, console, user, action_name='Healing', magic_type='Basic', mana_cost=20)
        
    def get_target_options(self):
        return self.user.team.get_teammembers()

    def display_health(self, name, hp):

        text = " {} was healed with {:.2f} health points!".format(name, hp)
        self.IOconsole.display_text(text)
        
    def execute(self, target):

        if self.user.get_mana() < self.spell_cost:
            mana_cost = self.user.get_mana()
        else:
            mana_cost = self.spell_cost
        
        hp = np.random.normal(mana_cost, 0.1*mana_cost)
        
        self.display_health(target.get_name(), hp)

        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_health(hp)
      

class ManaShield(Spell):
    def __init__(self, console, user):
        Spell.__init__(self, console, user, action_name='Mana Shield', magic_type='Basic', mana_cost=20)
        
    def get_target_options(self):
        return self.user.team.get_teammembers()

    def display_shield(self, name, defense):

        text = " {} has raised {:.2f} mana shield!".format(name, defense)
        self.IOconsole.display_text(text)
        
    def execute(self, target):

        if self.user.get_mana() < self.spell_cost:
            mana_cost = self.user.get_mana()
        else:
            mana_cost = self.spell_cost
            
        defense = np.random.normal(mana_cost, 0.1*mana_cost)  
        
        self.display_shield(target.get_name(), defense)

        # Update player stats
        self.user.set_mana(-mana_cost)
        target.set_defense(defense) 
        