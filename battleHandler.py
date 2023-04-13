import numpy as np # Import Numpy to perform statistics and numerical calculations
import player as p # Import Player library to load all the ai and players
import team as t
from itertools import chain
import IO

class battleHandler(object):
    """
    The battleHandler class is a simple game engine that contains
    the state of the game and the state of all players.

    Once created, game loop will continue until one of the teams
    is eliminated or the player quits the game. 
    """
    
    # Initialize the number of heroes and enemies to create
    def __init__(self, console):
        self.IOconsole = console
        self.continue_game_state = True
        self.random_number = None
        self.active_player = None
        self.total_player_speeds = 0
        self.action = None
        self.targets = None
        
    # Get current game state
    def get_continue_game_state(self):
        return self.continue_game_state
    
    # Update the game state
    def set_continue_game_state(self, state):
        self.continue_game_state = state
        
    # Get random number
    def get_random_number(self):
        return self.random_number
        
    # Get Random number between zero and the total speed of players 
    def set_random_number(self):
        high = self.get_total_player_speeds() + 1
        self.random_number = np.random.randint(0, high)
    
    # Get current active player
    def get_active_player(self):
        return self.active_player
    
    # Set current player to the active player
    def set_active_player(self, active_player):
        self.active_player = active_player
        
    # Get total player speed
    def get_total_player_speeds(self):
        return self.total_player_speeds
    
    # Set total player speed to total_speed
    def set_total_player_speeds(self, total_speed):
        self.total_player_speeds = total_speed
    
    # Get current action
    def get_action():
        return self.action
        
    # Set current action
    def set_action(action):
        self.action = action
    
    # Get targets
    def get_targets():
        return self.targets
    
    # Get set targets
    def set_targets(targets):
        self.targets = targets

    # Determine who goes first based on where the random number falls in range of roll numbers calculated
    def set_roll_numbers(self):
        
        # Keep track of the current total speed of characters to determine roll numbers (reset after every round)
        self.set_total_player_speeds(0)
        
        # Loop through players
        for player_name, player in chain(self.heroes.teammembers.items(), self.enemies.teammembers.items()):
            
            # Assign roll number based on the accumulated speed calculated so far (heros and enemies)
            self.set_total_player_speeds(self.get_total_player_speeds() + player.get_speed())
            player.set_roll_number(self.get_total_player_speeds())
        
    # Creates all the hero and enemy players to begin the game
    def init_teams(self):        
        
        # Initialize hero team objects
        self.heroes = t.team(console=self.IOconsole, team_name='Heroes')
        
        # Initialize enemy team objects
        self.enemies = t.team(console=self.IOconsole, team_name='Enemies') 
        
        # Set teams againts each other
        self.heroes.set_enemy(self.enemies)
        self.enemies.set_enemy(self.heroes)
        
        # Assigns roll numbers to each player
        self.set_roll_numbers()
    
    # Determine which player goes next
    def determine_active_player(self):
        
        # Loop through players
        for player_name, player in chain(self.heroes.teammembers.items(), self.enemies.teammembers.items()):
            
            # If random number falls within range of hero's roll number
            num = self.get_random_number()
            if num <= player.get_roll_number():
        
                # Assign turn to player
                self.set_active_player(player)
                break

    # Play game using randomized turn-based mechanics based on total speed of all players
    def fight(self):
        
        # Initialize both teams
        self.init_teams()
        
        # Get a random number
        self.set_random_number()

        # Begin game message
        self.IOconsole.display_title("Begin Battle!")
        
        # Continue playing game until continue_game flag is set to false
        while self.get_continue_game_state():  
            
            # Display game stats
            self.IOconsole.display_battle_stats(self.heroes, self.enemies)

            # Determine which player goes next
            self.determine_active_player()
            
            # Let player determine set of actions
            self.active_player.action()
            
            # If all heros or all enemies are eliminated
            if (len(self.heroes.get_teammembers()) <= 0 or len(self.enemies.get_teammembers()) <= 0):
                    
                # Set continue_game flag to false
                self.set_continue_game_state(False)
        
            # Game continues with new random number
            self.set_random_number()
            
            # Reset all players roll numbers
            self.set_roll_numbers()
        
        # Display "Game Over" sign
        self.IOconsole.display_title("Game Over")
