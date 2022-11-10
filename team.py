import inventory as inv
import skillstree as sktr
import numpy as np
import player as p

# Create basic player object
class team(object):
    
    def __init__(self, console, team_name, enemy=None):
        self.IOconsole = console
        self.team_name = team_name
        self.total_health = 0
        self.total_speed = 0
        self.teammembers = {}
        self.enemy = None
        self.init_players()

    # Initialize n-number of players
    def init_players(self):

        # Ask user for number of valid (1-6) heros to create
        num_players = self.valid_num_players()

        # Initialize hero objects
        self.create_players(num_players)

    # Get number of players to create
    def valid_num_players(self):
        
        num_players = 0
        valid_input = False
        
        # While the input is not a valid input repeat the prompt
        while (valid_input==False):
            try:
                num_players = int(input(" Enter Number of {} between 1-6: ".format(self.get_team_name())))
            except:
                print(" Invalid Response")
                continue
            else:
                if (num_players > 0 and num_players <= 6):
                    valid_input = True

        # Return number of players to create        
        return num_players

    # Initializes player objects 
    def create_players(self, num_players):
        
        # Loop through all the number of players to create
        for i in range(num_players):
            
            # Ask user for the name of a player
            player_name = ""
            
            while player_name not in self.get_teammembers() and ((len(player_name) < 2) or (len(player_name) > 8)):
                player_name = input(" Enter a Valid Name for Player {}: ".format(i+1))
       
            self.create_player(player_name)
                
    # If hero create hero object otherwise create a player object
    def create_player(self, player_name):
        
        if self.get_team_name() == 'Heroes':
            player = p.Hero(console=self.IOconsole, name=player_name, team=self)
        else:
            player = p.Player(console=self.IOconsole, name=player_name, team=self)
        
        self.add_teammember(player)

    # Get team name
    def get_team_name(self):
        return self.team_name

    # Get teams total health
    def get_total_health(self):
        return self.total_health

    # Update teams total health
    def set_total_health(self, health):
        self.total_health += health
        if self.get_total_health() < 0:
            self.total_health = 0

    # Get teams total speed
    def get_total_speed(self):
        return self.total_speed

    # Set teams total speed
    def set_total_speed(self, speed):
        self.total_speed += speed
        if self.get_total_speed() < 0:
            self.total_speed = 0

    # Get active active 
    '''
    def get_active_state(self):
        return self.active

    def set_active_state(self):
        if self.active == False:
            self.active = True
        else:
            self.active = False
    '''

    # Get list of all players on team
    def get_teammembers(self):
        return self.teammembers

    # Add player to team
    def add_teammember(self, player):
        player_name = player.get_name()
        
        if player_name not in self.teammembers:
            self.teammembers[player_name] = player
            self.set_total_health(player.health)
            self.set_total_speed(player.speed)
        else:
            print(" Player already exists!")

    # Remove player from team
    def remove_teammember(self, player):
        player_name = player.get_name()
        
        if player_name in self.teammembers:
            self.set_total_health(-player.get_health())
            self.set_total_speed(-player.get_speed())
            del self.teammembers[player_name]
        else:
            print(" Player does not exists!")
           
    # Get player from team 
    def get_teammember(self, player_name):
        return self.teammembers[player_name]
            
    # Set enemy
    def set_enemy(self, enemy):
        self.enemy = enemy
        
    # Get enemy
    def get_enemy(self):
        return self.enemy
    
    # Get list of enemy players
    def get_enemy_teammembers(self):
        return self.enemy.get_teammembers()
    
    # Get enemy from enemy list
    def get_enemy_teammember(self, player_name):
        return self.enemy.teammembers[player_name]
    
    



