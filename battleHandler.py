import numpy as np # Import Numpy to perform statistics and numerical calculations
import player as p # Import Player library to load all the ai and players
import team as t
from itertools import chain
import battleHandlerIO as IO

class battleHandler(object):
    
    # Initialize the number of heros and enemies to create
    def __init__(self):
        self.continue_game_state = True
        self.random_number = None
        self.active_player = None
        self.total_player_speeds = 0
        self.action = None
        self.targets = None
        self.IO = IO.BattleHanderIO()
        
    def get_continue_game_state(self):
        return self.continue_game_state
    
    def set_continue_game_state(self, state):
        self.continue_game_state = state
        
    def get_random_number(self):
        return self.random_number
        
    # Get Random number between zero and the total speed of players 
    def set_random_number(self):
        high = self.get_total_player_speeds() + 1
        self.random_number = np.random.randint(0, high)
        
    def get_active_player(self):
        return self.active_player
    
    def set_active_player(self, active_player):
        self.active_player = active_player
        
    def get_total_player_speeds(self):
        return self.total_player_speeds
    
    def set_total_player_speeds(self, total_speed):
        self.total_player_speeds = total_speed
        
    def get_action():
        return self.action
    
    def execute_action():
        pass
        
    def set_action(action):
        self.action = action
    
    def get_targets():
        return self.targets
    
    def set_targets(targets):
        self.targets = targets

    # Determine who goes first based on where random number falls in range of roll numbers calculated
    def set_roll_numbers(self):
        
        # Keep track of the current total speed of characters to determine roll numbers (reset after every round)
        self.set_total_player_speeds(0)
        
        # Loop through players
        for player_name, player in chain(self.heroes.teammembers.items(), self.enemies.teammembers.items()):
            
            # Assign roll number based on the accumulated speeds calculates so far (heros and enemies)
            self.set_total_player_speeds(self.get_total_player_speeds() + player.get_speed())
            player.set_roll_number(self.get_total_player_speeds())
        
    # Creates all the hero and enemy players to being the game
    def init_teams(self):        
        
        # Initialize hero team objects
        self.heroes = t.team('Heroes')
        
        # Initialize enemy team objects
        self.enemies = t.team('Enemies') 
        
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

        if self.set_active_player == None:
            print("No player was selected?")
            exit()


    # Play game using randomized turn-based mechanics based on all players' speeds
    def fight(self):
        
        # Begin Game Message
        self.IO.welcome_message()
        
        # Initialize both teams
        self.init_teams()
        
        # Get a random number
        self.set_random_number()
        
        # Continue playing game until continue_game flag is set to false
        while self.get_continue_game_state():  
            
            # Determine which player goes next
            self.determine_active_player()
            
            # Display game stats
            self.IO.battle_stats(self.active_player, self.heroes, self.enemies)
            
            # Let player determine set of actions
            self.active_player.action()
            
            # If all heros or all enemies are eliminated
            if (len(self.heroes.get_teammembers()) <= 0 or len(self.enemies.get_teammembers()) <= 0):
                    
                # Set continue_game flag to false
                self.set_continue_game_state(False)
        
            # Game Continues with new random number
            self.set_random_number()
            
            # Reset all players roll numbers
            self.set_roll_numbers()
        
        # Display "Game Over" Sign
        self.IO.game_over_message()


    