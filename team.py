import inventory as inv
import skillstree as sktr
import numpy as np
import player as p

# Create basic player object
class team(object):
    """
    The team class creates a data structure to keep track of
    each team and their total player stats.
    """
    
    def __init__(self, console, team_name, enemy=None):
        self.IOconsole = console
        self.team_name = team_name
        self.total_health = 0
        self.total_speed = 0
        self.teammembers = {}
        self.enemy = None
        self.max_team_size = 5
        self.init_players()

    # Initialize n-number of players
    def init_players(self):

        # Ask user for number of valid (1-6) heros to create
        title = " Enter Number of {} between 1-5: ".format(self.get_team_name())
        num_players = self.IOconsole.display_menu(title, self.max_team_size)

        # Initialize hero objects
        self.create_players(num_players)

    # Initialize player objects 
    def create_players(self, num_players):
        
        # Loop through all the number of players to create
        for i in range(num_players):
            
            # Ask user for the name of a player
            player_name = ""
            
            # While valid player name needs to be entered, keep requesting name from user
            while (player_name not in self.get_teammembers()) and ((len(player_name) < 2) or (len(player_name) > 8)):
                prompt = " Enter a Valid Name for Player {}: ".format(i+1)
                player_name = self.IOconsole.display_input(prompt)
       
            # Create player
            self.create_player(player_name)
                
    # If hero, create hero object, otherwise create a player object
    def create_player(self, player_name):
        
        # If player belongs to heroes, create hero object
        if self.get_team_name() == 'Heroes':
            player = p.Hero(console=self.IOconsole, name=player_name, team=self)
        
        # Else create regular player
        else:
            player = p.Player(console=self.IOconsole, name=player_name, team=self)
        
        # Add player to their respective team
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

    # Get list of all players on team
    def get_teammembers(self):
        return self.teammembers

    # Add player to team
    def add_teammember(self, player):
        player_name = player.get_name()
        
        # If player not already in team, add to team
        if player_name not in self.teammembers:
            self.teammembers[player_name] = player
            self.set_total_health(player.health)
            self.set_total_speed(player.speed)

        # Else notify user player already exist
        else:
            self.IOconsole.display_text(" Player already exists!", edge=False)

    # Remove player from team
    def remove_teammember(self, player):
        player_name = player.get_name()
        
        # Check if player in team
        if player_name in self.teammembers:
            self.set_total_health(-player.get_health())
            self.set_total_speed(-player.get_speed())
            del self.teammembers[player_name]

        # Else notify user player does not exist on team
        else:
            self.IOconsole.display_text(" Player does not exists!", edge=False)
           
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
